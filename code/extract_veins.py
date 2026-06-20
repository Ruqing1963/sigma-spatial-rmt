#!/usr/bin/env python3
"""
Extract quartz-carbonate vein intercepts from the GM 69917 drill-log PDF.

The four drill-hole logs (Appendices IV-VI) record each vein as a line of the
form:
    <from>  <to>  VN,<width>cm,...,<minerals>,...,<angle>deg,...
e.g.
    25.20 25.37 VN,9.00cm,%,Cb,Qz,CI,C,MA,40.00 ,Au%,Py8.00%,...

OCR quality differs between holes (commas read as dots, etc.), so a tolerant
regex is used. Holes are assigned by the line-number ranges of their log
appendices, determined from the appendix headers.

Requires: poppler-utils (pdftotext). Input PDF not redistributed here (public
report GM 69917, available from Quebec MRNF SIGEOM).

Usage:
    python3 extract_veins.py GM69917.pdf  > ../data/sigma_veins.csv
"""
import sys
import re
import subprocess
import csv

# Log-appendix line ranges (from the appendix headers in the -layout text).
# These were located by searching for "Appendix IV/V/VI - Log of ..." and the
# per-hole "DDH: SV-16-0xx" headers.
HOLE_RANGES = [
    ('LD-16-001A', 12331, 17690),
    ('SO-16-003',  17690, 18730),
    ('SV-16-009',  18741, 19579),
    ('SV-16-011',  19579, 20514),
]

VEIN_RE = re.compile(r'(\d+[.,]\d+)\s+(\d+[.,]\d+)\s+VN[.,L](\d+\.?\d*)\s*[noc]?m')
ANGLE_RE = re.compile(r'(\d+\.\d+)\s*["\u00b0~\'`]')
MINERAL_RE = re.compile(r'\b(Qz|Cb|Tour|Ti|Ab|Ep|Cc|Sr|Py|Po|Cp|Cl|Su)\b')


def hole_of(lineno):
    for name, lo, hi in HOLE_RANGES:
        if lo <= lineno < hi:
            return name
    return None


def main(pdf_path):
    txt = subprocess.run(
        ['pdftotext', '-layout', pdf_path, '-'],
        capture_output=True, text=True, timeout=180).stdout
    lines = txt.split('\n')

    w = csv.writer(sys.stdout)
    w.writerow(['hole', 'from_m', 'to_m', 'width_cm', 'angle_deg', 'minerals'])
    n = 0
    for i, line in enumerate(lines):
        hole = hole_of(i)
        if hole is None:
            continue
        m = VEIN_RE.search(line)
        if not m:
            continue
        frm = float(m.group(1).replace(',', '.'))
        to = float(m.group(2).replace(',', '.'))
        width = float(m.group(3))
        am = ANGLE_RE.search(line[m.end():])
        angle = float(am.group(1)) if am else ''
        minerals = ','.join(MINERAL_RE.findall(line[m.end():]))
        w.writerow([hole, frm, to, width, angle, minerals])
        n += 1
    print(f'# extracted {n} vein intercepts', file=sys.stderr)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: extract_veins.py GM69917.pdf', file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1])
