#!/usr/bin/env python3
"""Regenerate the finite majority tables printed in the manuscript.

The logarithmic table reports the exact finite-X lower bound 2 B_X - 1,
not only its asymptotic limit 1 - 2 theta.
"""
from pathlib import Path
import csv
import numpy as np
from common import load_liouville, lambda_at

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
lam = load_liouville()

m = 2
X = 10_000_000
n = np.arange(1, X + 1, dtype=np.int64)
nld = n.astype(np.longdouble)
weights = 1.0 / n.astype(np.float64)
H_X = float(weights.sum())
lam_n_i16 = lambda_at(lam, n).astype(np.int16)
lam_n_f64 = lam_n_i16.astype(np.float64)
lambda_m = int(lambda_at(lam, [m])[0])

natural_cs = [0.60, 0.90]
natural_rows = []
for c in natural_cs:
    alpha = np.longdouble(m) * np.expm1(np.longdouble(str(c)) / np.longdouble(X))
    offsets = np.floor(alpha * nld).astype(np.int64)
    idx = m * n + offsets
    vals = lam_n_i16 * lambda_at(lam, idx).astype(np.int16)
    C = int(vals.sum())
    I0 = min(X, int(np.ceil(np.longdouble(1) / alpha) - 1))
    finite_signed_lower = (2 * I0 - X) / X
    asymptotic_signed_lower = 2 * min(1.0, 1.0 / (m * c)) - 1.0
    natural_rows.append(
        (c, lambda_m * C / X, finite_signed_lower, asymptotic_signed_lower, I0)
    )

thetas = [0.00, 0.20, 0.40, 0.45]
log_rows = []
for theta in thetas:
    cX = float(X ** theta)
    scale = np.longdouble(m) * np.exp(np.longdouble(str(cX)) / np.longdouble(X))
    idx = np.floor(scale * nld).astype(np.int64)
    vals = lam_n_f64 * lambda_at(lam, idx).astype(np.float64)
    C_log = float(np.sum(weights * vals) / H_X)

    alpha = np.longdouble(m) * np.expm1(
        np.longdouble(str(cX)) / np.longdouble(X)
    )
    n0 = min(X, int(np.ceil(np.longdouble(1) / alpha) - 1))
    B_X = float(weights[:n0].sum() / H_X)
    finite_signed_lower = 2.0 * B_X - 1.0
    asymptotic_signed_lower = 1.0 - 2.0 * theta
    log_rows.append(
        (
            theta,
            cX,
            C_log,
            lambda_m * C_log,
            B_X,
            finite_signed_lower,
            asymptotic_signed_lower,
            n0,
        )
    )

csv_path = OUT / "paper_majority_tables_v2.csv"
with csv_path.open("w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["section", "parameter", "c_or_cX", "signed_measured",
                "B_or_I0", "finite_signed_lower", "asymptotic_signed_lower"])
    for c, signed, finite, asymptotic, I0 in natural_rows:
        w.writerow(["natural", c, c, f"{signed:.12f}", I0,
                    f"{finite:.12f}", f"{asymptotic:.12f}"])
    for theta, cX, Clog, signed, B, finite, asymptotic, n0 in log_rows:
        w.writerow(["logarithmic", theta, f"{cX:.12g}", f"{signed:.12f}",
                    f"{B:.12f}", f"{finite:.12f}",
                    f"{asymptotic:.12f}"])

txt_path = OUT / "paper_majority_tables_v2.txt"
with txt_path.open("w") as f:
    f.write("FINITE MAJORITY TABLES USED IN THE MANUSCRIPT\n")
    f.write("m=2, X=10,000,000, H_X normalization for C_log\n\n")
    f.write("Natural majority\n")
    f.write("c      lambda(2) C_X/X   finite lower   asymptotic lower   I0\n")
    for c, signed, finite, asymptotic, I0 in natural_rows:
        f.write(f"{c:0.2f}   {signed: .9f}       {finite: .9f}     "
                f"{asymptotic: .9f}       {I0}\n")
    f.write("\nLogarithmic mesoscopic majority\n")
    f.write("theta    c_X        C_log          lambda(2)C_log   B_X        "
            "2B_X-1       1-2theta\n")
    for theta, cX, Clog, signed, B, finite, asymptotic, n0 in log_rows:
        f.write(f"{theta:0.2f}   {cX:10.4f}  {Clog: .9f}   "
                f"{signed: .9f}      {B: .9f}  {finite: .9f}  "
                f"{asymptotic: .9f}\n")

print(txt_path.read_text())
