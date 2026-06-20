# Time–Space Asymmetry in Orogenic Gold Systems: Sigma Deposit Vein Spacing

**Repository:** https://github.com/Ruqing1963/sigma-spatial-rmt

This repository accompanies the paper:

**"Time–Space Asymmetry in Orogenic Gold Systems: Temporal Level Repulsion but
Spatial Clustering of Ore-Stage Veins at the Sigma Deposit, Val-d'Or, Canada"**
by Ruqing Chen (GUT Geoservice Inc., Montreal).

## Summary

This is Part II of the spatial racetrack in a research program applying Random
Matrix Theory (RMT) to Earth-system rhythms. The program's unifying principle:
**a single isolated long-memory process yields GOE/GUE level repulsion; the
superposition of many independent sources yields Poisson/clustered statistics.**

A previous racetrack showed that orogenic gold mineralization is **temporally**
repulsive (GOE) — a charge-and-release rhythm of a single deep fluid source.
This paper tests the **spatial** analog: do ore-stage extensional veins show
stress-shadow spatial repulsion?

**Result (negative for stress-shadow repulsion, but informative):** Using 235
quartz–carbonate vein intercepts logged in four diamond drill holes at the
Sigma orogenic gold deposit (public report GM 69917), the along-hole vein
spacing is **clustered, not repulsive**: pooled ⟨r⟩ = 0.344 (below Poisson
0.386), CV = 1.45 (> 1), with a systematic short-spacing excess. The GOE
hypothesis is rejected at p < 10⁻⁴.

This reveals a **time–space asymmetry**: the same orogenic gold system is
temporally repulsive but spatially clustered. The reconciliation: a single
*temporal* source (one deep fluid clock) corresponds to a *spatial*
superposition of inherited localization sites (structural inheritance +
crack–seal cycling).

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

- Racetrack 4 (metallogeny, temporal GOE incl. orogenic gold):
  https://zenodo.org/records/20768849
- Part I (spatial, cyclostratigraphy, GUE repulsion):
  https://zenodo.org/records/20774581
- Primes × strata companion: https://zenodo.org/records/20775610

## License

MIT (see LICENSE).
