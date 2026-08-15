# Reproducibility - FINAL v.2

The paper uses only `data/liouville_int8_N21000000.bin`, a raw signed-int8 prefix of the Liouville function with byte `n-1` equal to `lambda(n)` and `N = 21,000,000`.

The final audit regenerated all 21,000,000 bytes from `lambda(n)=(-1)^Omega(n)` and verified byte-for-byte equality with the supplied binary.

Numerical scripts:

    python3 src/verify_core_results.py
    python3 src/verify_rational_local_profile.py
    python3 src/verify_natural_majority.py
    python3 src/verify_logarithmic_mesoscopic.py
    python3 src/verify_finite_majority_tables.py

The last script independently regenerates the finite majority tables printed in the manuscript. In particular, the logarithmic table uses the exact finite-X bound `2 B_X - 1`; the asymptotic quantity `1 - 2 theta` is kept in a separate column and is not used as a finite-X theorem bound.

PNG figures:

    python3 src/plot_rational_resonances.py
    python3 src/plot_rational_profile.py
    python3 src/plot_logarithmic_mesoscopic.py

The logarithmic figure plots the exact finite-X majority bound, not the asymptotic limit.

Compile from `submission/`:

    pdflatex tex_resonant_liouville_JNT_FINAL_v2.tex
    pdflatex tex_resonant_liouville_JNT_FINAL_v2.tex
    pdflatex tex_resonant_liouville_JNT_FINAL_v2.tex

The supplied `elsarticle.cls` is the class used for compilation. Figures are PNG files only.
