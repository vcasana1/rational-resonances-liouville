ABSTRACT_ADD = r"""
In this expanded version the two-point input is supplied by the ordinary
two-point theorem of OpenAI (2026), which makes the natural profile
unconditional with the rate $(\log X)^{-\kappa}$. We introduce the $k$-point
resonance family, prove its exact decomposition into proportionality classes
and its closed-form profile, extend the plateaus, the majority theorem and the
left-hand identity to every $k$, and show that the level-three family at the
resonances $(2,3)$ is, for every large $X$, the ordinary three-point sum
$\sum_{M\equiv3\,(6)}\lambda(M)\lambda(M+1)\lambda(M+3)$. For the bias method
behind the two-point theorem we prove that its centering step cannot be
extended to $k\ge3$ with the short-interval input it uses, that local $U^k$
uniformity suffices for that step, and that a quantitative local Gowers
uniformity hypothesis together with a $k$-linear divisor-graph hypothesis
yields $k$-point Chowla in progressions and the profile of the whole family.
"""

INTRO_ADD = r"""
\paragraph{Expanded version}
Sections~\ref{sec:unconditional}--\ref{sec:three} are new. The remainder of
the residue-class decomposition is a finite set of fixed binary affine
correlations, and the ordinary two-point Chowla theorem of
\cite[Theorem~1.1, p.~3]{OpenAI2026} controls exactly these; Section~\ref{sec:unconditional}
records the resulting unconditional profile with a rate, and shows that at the
trivial resonance $p=q=1$, $-1<c<0$, the profile is literally the shift-one
Chowla sum. Section~\ref{sec:kpoint} constructs the $k$-point family
$C^{(k)}_X$, proves its exact decomposition (Theorem~\ref{thm:dec_k}), the
criterion for unconditional closure (Proposition~\ref{prop:criterion}), the
plateau, majority and left-hand identities at every level
(Theorem~\ref{thm:integer_k}), the identification of level three at $(2,3)$
with an ordinary three-point Chowla sum (Corollary~\ref{cor:level3_23}), and
the necessity theorem (Theorem~\ref{thm:nec_k}). Section~\ref{sec:three}
examines the bias method of \cite[Part~II]{OpenAI2026} for $k\ge3$ points:
a barrier for its centering step (Propositions~\ref{prop:barrier_poly}
and~\ref{prop:barrier_pos}), an unconditional bound of the $k$-point centering
error by local Gowers norms (Proposition~\ref{prop:local_control}), and a
conditional $k$-point theorem (Theorem~\ref{thm:conditional_k},
Corollary~\ref{cor:family_conditional}) whose two hypotheses are stated
explicitly and are not proved here.
"""

REMARK_SEC2 = r"""
\begin{remark}[Status of Conjecture~\ref{conj:affine_chowla}]
\label{rem:status_conj}
For non-negative intercepts, Conjecture~\ref{conj:affine_chowla} is now
\cite[Theorem~1.1, p.~3]{OpenAI2026}, with a power-of-logarithm saving at
every real cutoff; negative intercepts reduce to that case by a fixed shift
(Lemma~\ref{lem:macro_rate}). Sections~\ref{sec:rational}--\ref{sec:integer}
are kept in their original conditional formulation; the unconditional
statements are collected in Section~\ref{sec:unconditional}.
\end{remark}
"""

CONCL_ADD = r"""

With the ordinary two-point theorem of \cite{OpenAI2026} the natural profile
is unconditional, with the rate $(\log X)^{-\kappa}$, because its remainder is
a finite set of fixed binary correlations. At level $k\ge3$ the exact
decomposition reduces every block to a $k'$-point correlation with
$k'\equiv k\pmod2$; blocks with $k'\le2$ are unconditional, and the
left-hand identity shows that blocks with $k'\ge3$ are genuine, for every
large $X$: level three at $(2,3)$ is the ordinary sum
$\sum_{M\equiv3\,(6)}\lambda(M)\lambda(M+1)\lambda(M+3)$. In the bias method
the centering step is controlled by local $U^k$ norms, and cannot be
controlled by the averaged short exponential sums used for two points; the
graph step requires a $k$-linear divisor-graph estimate. Both inputs are
isolated as hypotheses.
"""

BIB_ADD = r"""
\bibitem{CasanaPadic}
V. Casa\~na-Giner,
\textit{Exact $p$-adic martingale shells and finite-conductor encodings},
manuscript (padic\_shells), 2026; \textit{Theorems and Their Proofs}, compendium of 25 October 2026, entries 48.0.32--48.0.36, pp.~884--887.

\bibitem{Gowers2001}
W.~T. Gowers,
\textit{A new proof of Szemer\'edi's theorem},
Geom. Funct. Anal. 11 (2001), 465--588;
DOI: \href{https://doi.org/10.1007/s00039-001-0332-9}{10.1007/s00039-001-0332-9}.

\bibitem{MRT2020}
K. Matom\"aki, M. Radziwi{\l}{\l}, T. Tao,
\textit{Fourier uniformity of bounded multiplicative functions in short intervals on average},
Invent. Math. 220 (2020), 1--58;
DOI: \href{https://doi.org/10.1007/s00222-019-00926-w}{10.1007/s00222-019-00926-w};
arXiv:\href{https://arxiv.org/abs/1812.01224}{1812.01224}.

\bibitem{OpenAI2026}
OpenAI,
\textit{Ordinary two-point correlations of multiplicative functions},
preprint, 24 September 2026, 87 pp.; no DOI.

\bibitem{Tao2017}
T. Tao,
\textit{Equivalence of the logarithmically averaged Chowla and Sarnak conjectures},
in: Number Theory -- Diophantine Problems, Uniform Distribution and Applications,
Springer, Cham, 2017, pp.~391--421;
DOI: \href{https://doi.org/10.1007/978-3-319-55357-3_21}{10.1007/978-3-319-55357-3\_21};
arXiv:\href{https://arxiv.org/abs/1605.04628}{1605.04628}.

\bibitem{TaoTeravainen2018}
T. Tao, J. Ter\"av\"ainen,
\textit{Odd order cases of the logarithmically averaged Chowla conjecture},
J. Th\'eor. Nombres Bordeaux 30 (2018), 997--1015;
DOI: \href{https://doi.org/10.5802/jtnb.1062}{10.5802/jtnb.1062};
arXiv:\href{https://arxiv.org/abs/1710.02112}{1710.02112}.
"""
