# Sigma Orogenic Gold Vein Spacing — Spatially Clustered, Not Repulsive

**Repository:** https://github.com/Ruqing1963/sigma-spatial-rmt

> **Version 2.0 (2026-06-27).** The spatial analysis is unchanged. The *temporal*
> framing is corrected: v1's "temporal level repulsion (GOE) / time–space
> asymmetry" is replaced by **temporal scalar clock + spatial clustering**, per
> the audit [10.5281/zenodo.20980670](https://doi.org/10.5281/zenodo.20980670).
> See `CHANGELOG.md`; the v1 PDF is preserved in `paper/archive/v1/`.

This repository accompanies the paper:

**"Ore-Stage Veins at the Sigma Orogenic Gold Deposit Are Spatially Clustered,
Not Stress-Shadow Repulsive: a Drill-Core Test, and Why Declustering Fabricates
GOE (Val-d'Or, Abitibi, Canada)"** by Ruqing Chen (GUT Geoservice Inc., Montreal).

## Summary

This study tests how event-spacing statistics depend on single-source versus
superposed-source configurations. The robust limb of the program is
**superposition → Poisson**. A single "charge-and-release" source is a relaxation
oscillator whose timing is a narrow **scalar clock** (a high but
shuffle-invariant spacing ratio), **not** GOE level repulsion — see the audit
[10.5281/zenodo.20980670](https://doi.org/10.5281/zenodo.20980670). This paper
tests the **spatial** record of the same deposit class: do ore-stage extensional
veins show stress-shadow spatial repulsion?

**Result (negative for stress-shadow repulsion, but informative):** Using 235
quartz–carbonate vein intercepts logged in four diamond drill holes at the
Sigma orogenic gold deposit (public report GM 69917), the along-hole vein
spacing is **clustered, not repulsive**: pooled ⟨r⟩ = 0.344 (below Poisson
0.386), CV = 1.45 (> 1), with a systematic short-spacing excess. The GOE
hypothesis is rejected at p < 10⁻⁴.

The same orogenic gold system therefore pairs a **temporal scalar clock** with
**spatial clustering** (a superposition of inherited localization sites by
structural inheritance and crack–seal cycling). A single temporal source need
not be a single spatial source; the temporal leg is a scalar clock, not level
repulsion.

## Key results

| Drill hole | n | ⟨r⟩ | CV |
|---|---|---|---|
| LD-16-001A | 122 | 0.347 | 1.63 |
| SO-16-003 | 53 | 0.367 | 1.17 |
| SV-16-009 | 37 | 0.329 | 1.09 |
| SV-16-011 | 23 | 0.325 | 0.81 |
| **Pooled** | **235** | **0.344** | **1.45** |
| Poisson (ref) | | 0.386 | 1.00 |
| GOE (ref) | | 0.536 | <1 |

Independent corroboration: Lilstock mapped fracture network (CV = 1.52) and
published vein arrays (CV = 1.20–1.69) are likewise clustered.

## Methodological warning

**Minimum-separation declustering fabricates spurious GOE statistics.** Applying
it to *pure random points* drives ⟨r⟩ to the GOE value just as readily as for
real veins (see `code/analyze_sigma_veins.py`, control section, and Fig. 1d).
The honest diagnostic is the **raw spacing-ratio ⟨r⟩ together with CV**, with
no point removal. This repository uses no declustering for any scientific claim.

## Repository layout

```
code/    analyze_sigma_veins.py   reproducible analysis + declustering control
         extract_veins.py         vein extraction from the GM 69917 PDF logs
data/    sigma_veins.csv          235 vein intercepts (hole, from, to, width, angle, minerals)
         sigma_veins_4holes.json  same data as JSON
figures/ sigma_partII_figure.png  four-panel result figure
paper/   sigma_spatial_rmt.tex    LaTeX source
         sigma_spatial_rmt.pdf    compiled paper
```

## Data source

Vein positions were extracted from the public assessment report **GM 69917**
(Or Integra Quebec Inc., 2016, Sigma-Lamaque property, NTS 32C/04), available
from the Quebec MRNF SIGEOM/GESTIM system. Sigma orebody location: UTM Zone 18,
294737 E, 5331127 N. Deposit classification: orogenic auriferous veins.

## Reproduce

```bash
pip install -r requirements.txt
cd code && python3 analyze_sigma_veins.py
```

## Related work in this program

- **Temporal audit (erratum basis for this v2):** Narrow scalar clocks, not level
  repulsion — https://doi.org/10.5281/zenodo.20980670 (shows the ore-timing
  "temporal GOE" is a scalar clock; basis for the v2 reframing here).
- Metallogeny four-province timing (the audited study):
  https://zenodo.org/records/20768849
- Spurious level repulsion (declustering / seasonal gating / Wishart):
  https://doi.org/10.5281/zenodo.20883107

## License

MIT (see LICENSE).
