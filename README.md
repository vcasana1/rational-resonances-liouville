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

## Expanded version expanded_lio_v1 (7 November 2026)

[Sections 7--9](developments/2026-11-07-expanded-lio-v1/): unconditional
profile with rate via the OpenAI two-point theorem, the k-point resonance
family, and the centering step of the bias method for k >= 3 (barriers,
local Gowers control, conditional theorem under two stated hypotheses).

- [TEX](developments/2026-11-07-expanded-lio-v1/expanded_lio_v1.tex)
- [TXT](developments/2026-11-07-expanded-lio-v1/expanded_lio_v1.txt)
- [PDF](developments/2026-11-07-expanded-lio-v1/expanded_lio_v1.pdf)
- [ZIP](developments/2026-11-07-expanded-lio-v1/expanded_lio_v1.zip)

## Expanded version expanded_lio_v2 (7 November 2026)

[expanded_lio_v2](developments/2026-11-07-expanded-lio-v2/): Sections 7--9 on
top of the submitted v2 text, plus the channel-form remark (9.11).

- [TEX](developments/2026-11-07-expanded-lio-v2/expanded_lio_v2.tex)
- [TXT](developments/2026-11-07-expanded-lio-v2/expanded_lio_v2.txt)
- [PDF](developments/2026-11-07-expanded-lio-v2/expanded_lio_v2.pdf)
- [ZIP](developments/2026-11-07-expanded-lio-v2/expanded_lio_v2.zip)
