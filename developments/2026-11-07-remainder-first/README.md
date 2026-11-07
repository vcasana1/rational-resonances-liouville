# Remainder-first derivation

The mathematical text is entirely in English. The original resonance
manuscript and the supplied OpenAI manuscript have not been modified.

This derivation starts with the nonproportional affine blocks in the
resonance paper, before introducing the analytic machinery. It proves
the following chain:

1. Define the actual block remainder and identify the unique proportional block.
2. Convert each nonproportional block exactly to a fixed-shift progression interval.
3. Develop centering, operator transfer, graph testing, endpoint control and constant selection.
4. Close the block remainder using explicitly cited intermediate estimates of the supplied manuscript.
5. Recover fixed-shift two-point Chowla from the negative microscopic remainders, by induction on the shift.
6. Complete the natural microscopic profile with the quantitative remainder bound.

The final affine theorem of `final.pdf` and its final progression theorem
are not used as inputs. No full source section is copied or appended.

## Exact scope

The proof imports the Fourier and short-sum estimates in Lemma 4.2 and
Theorem 4.3, the deletion estimate in Lemma 4.6 with the prohibited-path
construction, the nonbacktracking moment in Theorem 5.4, and the
truncated integer weight bound in Corollary 3.3 of the supplied `final.pdf`.
The consequences of these inputs are developed in the text. Their full
sieve, finite-law and closed-walk proofs are not re-proved here.

Accordingly, this is a proof using stated intermediate results of the
supplied manuscript. It is not a self-contained independent proof of
two-point Chowla and is not an independent certification that those
intermediate results are valid. No historical dependence or priority
claim about the OpenAI manuscript follows from this application.

## Files

- `REMAINDER_FIRST_PROOF.pdf`: the mathematical text.
- `REMAINDER_FIRST_PROOF.tex`: editable source, without external included sections.
- `REMAINDER_FIRST_PROOF.txt`: readable plain-text edition, retaining mathematical expressions in LaTeX notation.
- `QA/export_plain_text.py`: reproducible TXT exporter.
- `QA/check_exact_identities.py`: reproducible finite checks of the new exact block and band identities.
- `QA/EXACT_IDENTITY_CHECKS.json`: their output; finite checks do not prove the asymptotic bounds.
- `QA/SOURCE_PROVENANCE.json`: hashes and local source pointers.
- `QA/BUILD/`: compiler output.
- `QA/page-*.png` and `QA/contact-*.png`: rendered-page inspection artifacts.
- `MANIFEST_SHA256.txt`: package integrity manifest.

The portable ZIP contains the TEX, TXT and PDF, this README, the export
and identity-check scripts, the check report, source hashes and a package
manifest. Compiler output and rendered-page inspection images are kept
in the local QA directory and are omitted from the portable ZIP.

## Build

Run from this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=QA/BUILD REMAINDER_FIRST_PROOF.tex
cp QA/BUILD/REMAINDER_FIRST_PROOF.pdf REMAINDER_FIRST_PROOF.pdf
```

## Provenance of the route

One route is developed: an adaptation of the supplied centered-graph
method to the author's remainder. The exact conversion and the
negative-band extraction are deductions written out here. No independent
route outside that analytic method is established or claimed.
