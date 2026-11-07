import re, sys
sys.path.insert(0,'.')
from adds import *
src=open('/home/claude/rational-resonances-liouville/submission/tex_resonant_liouville_JNT_FINAL_v2.tex').read()
new=open('new_sections_v2.tex').read()

PRE = r"""\usepackage{graphicx}
\usepackage{array}
\usepackage[dvipsnames]{xcolor}
\usepackage[pagebackref=true]{hyperref}
\usepackage{bookmark}
\usepackage{pdfcomment}

% Hover previews for internal references (no layout change).
\makeatletter
\let\CG@origref\ref
\let\CG@origeqref\eqref
\newcommand{\CG@gettip}[1]{\@ifundefined{CGTip@#1}{Reference: #1}{\csname CGTip@#1\endcsname}}
\DeclareRobustCommand{\CGref}[1]{\pdftooltip{\CG@origref{#1}}{\CG@gettip{#1}}}
\DeclareRobustCommand{\CGeqref}[1]{\pdftooltip{\CG@origeqref{#1}}{\CG@gettip{#1}}}
%%TIPS%%
\makeatother

\hypersetup{
  colorlinks=false,
  pdfborder={0 0 1},
  linkbordercolor={1 0 0},
  citebordercolor={0 0.3 1},
  urlbordercolor={0 0.6 0.6},
  filebordercolor={0 0.6 0.6},
  linktoc=all,
  bookmarksnumbered=true,
  bookmarksopen=true,
  bookmarksopenlevel=1,
  pdfstartview=FitH,
  pdftitle={Rational Resonances and Microscopic Natural--Logarithmic Profiles for the Liouville Function (expanded version)},
  pdfauthor={V. Casa\~na-Giner},
  pdfsubject={Liouville function, Chowla conjecture, rational resonances, k-point family},
  pdfkeywords={Liouville function; Chowla conjecture; rational resonance; microscopic profile; local Gowers uniformity; divisor graph}
}
% Back-references in the bibliography.
\renewcommand*{\backref}[1]{}
\renewcommand*{\backrefalt}[4]{%
  \ifcase #1 %
    \relax
  \or
    \ (Cited on p.~#2.)%
  \else
    \ (Cited on pp.~#2.)%
  \fi}
"""
s=src
s=s.replace("\\usepackage{graphicx}\n\\usepackage[hidelinks]{hyperref}\n", PRE)
s=s.replace("\\setcounter{secnumdepth}{3}","\\setcounter{secnumdepth}{3}\n\\setcounter{tocdepth}{3}")
s=s.replace(r"""\newtheorem{conjecture}[theorem]{Conjecture}
""",r"""\newtheorem{conjecture}[theorem]{Conjecture}

\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{hypothesis}[theorem]{Hypothesis}
\newtheorem{example}[theorem]{Example}
""")
# abstract
s=s.replace(r"""majority rigidity.
\end{abstract}""","majority rigidity.\n"+ABSTRACT_ADD.strip()+"\n\\end{abstract}")
s=s.replace(r"""\end{frontmatter}""",r"""\end{frontmatter}

\tableofcontents""")
# intro
s=s.replace(r"""remaining pieces require affine Chowla cancellation.
""","remaining pieces require affine Chowla cancellation.\n"+INTRO_ADD)
# remark end sec2
s=s.replace(r"""\section{Exact rational decomposition}""",REMARK_SEC2.strip()+"\n\n\\section{Exact rational decomposition}")
# new sections
s=s.replace(r"""\section{Numerical verification}""",new.strip()+"\n\n\\section{Numerical verification}")
# conclusions
s=s.replace(r"""remain separated explicitly throughout.
""","remain separated explicitly throughout.\n"+CONCL_ADD)
# bib: DOIs as links, add entries (alphabetical-ish: append before end)
s=re.sub(r"DOI: \\nolinkurl\{([^}]*)\}",lambda m:"DOI: \\href{https://doi.org/%s}{%s}"%(m.group(1),m.group(1)),s)
s=re.sub(r"arXiv:(\d{4}\.\d{4,5})(?=[.;\n])",lambda m:"arXiv:\\href{https://arxiv.org/abs/%s}{%s}"%(m.group(1),m.group(1)),s)
s=s.replace(r"""\end{thebibliography}""",BIB_ADD.strip()+"\n\n\\end{thebibliography}")
# displays \[ \] -> numbered equations
cnt=[0]
def repl(m):
    cnt[0]+=1
    body=m.group(1).strip('\n')
    return "\\begin{equation}\n%s\n\\label{eq:o%d}\n\\end{equation}"%(body,cnt[0])
s=re.sub(r"(?<!\\)\\\[(.*?)(?<!\\)\\\]",repl,s,flags=re.S)
# refs -> CGref
s=re.sub(r"\\eqref\{",r"\\CGeqref{",s)
s=re.sub(r"(?<![a-zA-Z@])\\ref\{",r"\\CGref{",s)

# ---------- tooltips ----------
def flat(t,limit=900):
    t=re.sub(r"\\label\{[^}]*\}","",t)
    t=re.sub(r"\\(CG)?(eq)?ref\{([^}]*)\}",r"[\3]",t)
    t=re.sub(r"\\cite\[[^\]]*\]\{[^}]*\}","[ref]",t)
    t=re.sub(r"\\cite\{[^}]*\}","[ref]",t)
    t=re.sub(r"\\begin\{(cases|array|tabular|enumerate|center)\}(\{[^}]*\})?"," ",t)
    t=re.sub(r"\\end\{[a-z*]+\}"," ",t)
    t=re.sub(r"\\begin\{[a-z*]+\}"," ",t)
    t=re.sub(r"\\item"," ; ",t)
    t=re.sub(r"\\(mathbb|mathcal|mathrm|operatorname|textup|text|emph|textit|mathbf|mathfrak|mathsf)\{([^}]*)\}",r"\2",t)
    t=re.sub(r"\\d?frac\{([^{}]*)\}\{([^{}]*)\}",r"(\1)/(\2)",t)
    t=re.sub(r"\\(left|right|Bigl|Bigr|bigl|bigr|big|Big|biggl|biggr)\b","",t)
    t=re.sub(r"\\(,|;|!|:|quad|qquad| )"," ",t)
    t=t.replace("\\\\"," ")
    t=re.sub(r"\\([a-zA-Z]+)",r"\1",t)
    t=t.replace("\\","")
    t=t.replace("{","").replace("}","").replace("$","")
    t=re.sub(r"\s+"," ",t).strip()
    if len(t)>limit: t=t[:limit].rsplit(" ",1)[0]+" ..."
    t=t.replace("&"," ").replace("%"," percent ").replace("#"," ")
    t=t.replace("_","\\_").replace("^","\\textasciicircum{}").replace("~","\\textasciitilde{}")
    return t

envnames={'theorem':'Theorem','proposition':'Proposition','lemma':'Lemma','corollary':'Corollary','conjecture':'Conjecture','remark':'Remark','definition':'Definition','hypothesis':'Hypothesis','example':'Example','experiment':'Experiment'}
tips={}
# theorem-like
for m in re.finditer(r"\\begin\{(%s)\}(\[((?:[^\[\]]|\{[^{}]*\})*)\])?(.*?)\\end\{\1\}"%"|".join(envnames),s,flags=re.S):
    body=m.group(4); lab=re.search(r"\\label\{([^}]*)\}",body)
    if not lab: continue
    title=flat(m.group(3) or "",200)
    tips[lab.group(1)]="%s%s: %s"%(envnames[m.group(1)]," - "+title if title else "",flat(body))
for m in re.finditer(r"\\begin\{(equation|align)\}(.*?)\\end\{\1\}",s,flags=re.S):
    for lab in re.findall(r"\\label\{([^}]*)\}",m.group(2)):
        tips[lab]="Equation: "+flat(m.group(2))
for m in re.finditer(r"\\(section|subsection)\{((?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*)\}\s*\\label\{([^}]*)\}",s):
    tips[m.group(3)]=("Section: " if m.group(1)=="section" else "Subsection: ")+flat(re.sub(r"\\texorpdfstring\{([^}]*)\}\{[^}]*\}",r"\1",m.group(2)),200)
for m in re.finditer(r"\\caption\{(.*?)\}\s*\\label\{([^}]*)\}",s,flags=re.S):
    tips[m.group(2)]="Figure: "+flat(m.group(1))
labels=re.findall(r"\\label\{([^}]*)\}",s)
missing=[l for l in labels if l not in tips]
print("labels",len(labels),"tips",len(tips),"missing",missing)
tipdefs="\n".join("\\expandafter\\gdef\\csname CGTip@%s\\endcsname{%s}"%(k,v) for k,v in tips.items())
s=s.replace("%%TIPS%%",tipdefs)
# undefined refs check
refs=set(re.findall(r"\\CG(?:eq)?ref\{([^}]*)\}",s))
print("undefined refs:",sorted(refs-set(labels)))
open('expanded_lio_v2.tex','w').write(s)
