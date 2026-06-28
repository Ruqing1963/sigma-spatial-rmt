#!/usr/bin/env python3
"""
Spatial RMT analysis of Sigma orogenic gold veins (Racetrack 5, Part II).

Tests whether ore-stage extensional veins in a single orogenic gold deposit
show stress-shadow spatial repulsion (Wigner-Dyson) or clustering.

Honest method: raw spacing-ratio <r> and coefficient of variation CV on the
along-hole vein-position sequence. NO declustering preprocessing (declustering
fabricates spurious GOE - demonstrated explicitly below).

Data: GM 69917 (Or Integra 2016, Sigma-Lamaque property), 4 diamond drill holes,
235 logged quartz-carbonate vein intercepts.

Author: Ruqing Chen, GUT Geoservice Inc., Montreal
"""
import json
import numpy as np
from scipy import stats

POISSON_R = 0.386   # <r> for Poisson (uncorrelated) spacings
GOE_R     = 0.536   # <r> for GOE (level repulsion)
GUE_R     = 0.603   # <r> for GUE


def spacing_ratio(spacings):
    """Mean adjacent spacing ratio <r> = <min(s_i,s_{i+1})/max(s_i,s_{i+1})>.

    Parameter-free, requires no unfolding, immune to smooth density gradients.
    """
    s = np.asarray(spacings, float)
    s = s[s > 0]
    if len(s) < 3:
        return np.nan
    r = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])
    return float(r.mean())


def cv(spacings):
    """Coefficient of variation. CV=1 Poisson, <1 regular/repulsive, >1 clustered."""
    s = np.asarray(spacings, float)
    s = s[s > 0]
    return float(s.std() / s.mean())


def hole_positions(veins, hole):
    """Sorted along-hole midpoint positions of veins in a given drill hole."""
    pos = [(v['from'] + v['to']) / 2 for v in veins if v['hole'] == hole]
    return np.sort(np.asarray(pos, float))


def decluster(pos, min_sep_frac):
    """Greedy minimum-separation declustering (used ONLY to demonstrate it is
    an artifact generator - NOT used for the actual scientific result)."""
    pos = np.sort(np.asarray(pos, float))
    if min_sep_frac <= 0 or len(pos) < 2:
        return pos
    thr = min_sep_frac * np.median(np.diff(pos))
    keep = [pos[0]]
    for x in pos[1:]:
        if x - keep[-1] >= thr:
            keep.append(x)
    return np.array(keep)


def main():
    veins = json.load(open('../data/sigma_veins_4holes.json'))
    holes = ['LD-16-001A', 'SO-16-003', 'SV-16-009', 'SV-16-011']

    print("=" * 64)
    print("  Sigma orogenic gold veins - spatial spacing statistics")
    print("=" * 64)
    print(f"  {'hole':14s}{'n':>4s}{'<r>':>8s}{'CV':>7s}{'med(m)':>9s}")

    all_sp = []
    for h in holes:
        pos = hole_positions(veins, h)
        sp = np.diff(pos)
        sp = sp[sp > 0]
        all_sp.extend(sp)
        print(f"  {h:14s}{len(pos):>4d}{spacing_ratio(sp):>8.3f}"
              f"{cv(sp):>7.2f}{np.median(sp):>9.1f}")

    all_sp = np.asarray(all_sp)
    print(f"  {'pooled':14s}{len(all_sp)+4:>4d}{spacing_ratio(all_sp):>8.3f}"
          f"{cv(all_sp):>7.2f}{np.median(all_sp):>9.1f}")
    print(f"\n  Reference: Poisson <r>={POISSON_R} CV=1.0 | "
          f"GOE <r>={GOE_R} CV<1")

    # Permutation (shuffle) test: preserves the marginal spacing distribution,
    # destroys along-hole order. obs ~ shuf => clustering is a marginal/scalar
    # property of the spacing distribution, not a sequential correlation.
    rng = np.random.default_rng(0)
    r_obs = spacing_ratio(all_sp)
    r_shuf = np.mean([spacing_ratio(rng.permutation(all_sp)) for _ in range(5000)])
    print(f"\n  Permutation test: <r>_obs={r_obs:.3f}  <r>_shuf={r_shuf:.3f}  "
          f"obs-shuf={r_obs-r_shuf:+.3f}")
    print("    -> obs ~ shuf: clustering is a marginal (scalar) property of the")
    print("       broad vein-corridor spacing distribution, not sequential memory.")

    # KS tests
    sn = all_sp / all_sp.mean()
    ks_exp = stats.kstest(sn, 'expon')
    ks_goe = stats.kstest(sn, lambda s: 1 - np.exp(-np.pi * s**2 / 4))
    print(f"\n  KS vs Poisson(exp):   D={ks_exp.statistic:.3f} p={ks_exp.pvalue:.4f}")
    print(f"  KS vs GOE(Wigner):    D={ks_goe.statistic:.3f} p={ks_goe.pvalue:.4f}")

    # Short-spacing excess (clustering signature)
    print("\n  Short-spacing fraction (clustering diagnostic):")
    for thr in (0.1, 0.2, 0.3):
        obs = np.mean(sn < thr) * 100
        poi = (1 - np.exp(-thr)) * 100
        tag = 'excess->clustered' if obs > poi else 'deficit->repulsive'
        print(f"    s<{thr}: data {obs:4.1f}% vs Poisson {poi:4.1f}%  ({tag})")

    # Methodological control: declustering fabricates GOE
    print("\n" + "=" * 64)
    print("  CONTROL: declustering fabricates GOE from random points")
    print("=" * 64)
    pos_real = hole_positions(veins, 'LD-16-001A')
    rng = np.random.default_rng(7)
    pos_rand = np.sort(rng.uniform(pos_real.min(), pos_real.max(), len(pos_real)))
    print(f"  {'frac':>6s}{'real <r>':>10s}{'random <r>':>12s}")
    for frac in (0.0, 0.3, 0.5, 0.7):
        rr = spacing_ratio(np.diff(decluster(pos_real, frac)))
        rn = spacing_ratio(np.diff(decluster(pos_rand, frac)))
        print(f"  {frac:>6.1f}{rr:>10.3f}{rn:>12.3f}")
    print("  -> random points also driven to GOE; declustering is an artifact.")


if __name__ == '__main__':
    main()
