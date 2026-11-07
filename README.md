# Rational Resonances and Microscopic Natural--Logarithmic Profiles for the Liouville Function

Final v.2 Journal of Number Theory short-notice submission and reproducibility pack.

## Submission
- `submission/tex_resonant_liouville_JNT_FINAL_v2.tex`
- `submission/tex_resonant_liouville_JNT_FINAL_v2.pdf`
- `submission/elsarticle.cls`
- `submission/elsarticle-num.bst`
- three manuscript figures, PNG only

## Reproducibility
- `src/`: every Python script used for numerical checks and figure generation
- `data/liouville_int8_N21000000.bin`: the only binary used
- `outputs/`: literal Python stdout captures, CSV/TXT numerical outputs, LaTeX compilation logs, binary regeneration audit, and PDF preflight/render checks
- `figures/`: PNG figures only
- `checksums/`: SHA-256 inventories

The Liouville binary was regenerated from `lambda(n)=(-1)^Omega(n)` and verified byte-for-byte against the supplied data file before packaging.

No zeta/RVM binaries are used or included.

## Remainder-first development (7 November 2026)

The [dated development](developments/2026-11-07-remainder-first/) starts
from the resonance paper's nonproportional block remainder and develops
its closure and the recovery of fixed-shift two-point cancellation. It
uses explicitly identified intermediate estimates of the supplied OpenAI
manuscript; it is not a self-contained independent verification of those
estimates. The original submission is preserved.

- [TEX](developments/2026-11-07-remainder-first/REMAINDER_FIRST_PROOF.tex)
- [TXT](developments/2026-11-07-remainder-first/REMAINDER_FIRST_PROOF.txt)
- [PDF](developments/2026-11-07-remainder-first/REMAINDER_FIRST_PROOF.pdf)
- [ZIP](developments/2026-11-07-remainder-first/LIOUVILLE_REMAINDER_FIRST_20261107.zip)
