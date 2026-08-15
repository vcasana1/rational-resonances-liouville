# Reproduction - FINAL v.2

The manuscript uses only `data/liouville_int8_N21000000.bin`.

1. Install the packages listed in `requirements.txt`.
2. Regenerate numerical checks:

   `python src/verify_core_results.py`

   `python src/verify_rational_local_profile.py`

   `python src/verify_natural_majority.py`

   `python src/verify_logarithmic_mesoscopic.py`

   `python src/verify_finite_majority_tables.py`

3. Regenerate PNG figures with the three `src/plot_*.py` scripts.
4. Regenerate the Liouville binary independently with:

   `python src/generate_liouville_bin.py --N 21000000 --out data/liouville_int8_N21000000_regenerated.bin`

   `outputs/binary_regeneration_audit_v2.txt` records the byte-for-byte comparison performed for this archived version.
5. Compile from `submission/` with the supplied Elsevier class:

   `pdflatex tex_resonant_liouville_JNT_FINAL_v2.tex`

   Run three passes.

All manuscript figures are PNG files. No standalone figure is supplied as PDF.
