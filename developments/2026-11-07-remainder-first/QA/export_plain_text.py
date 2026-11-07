"""Export readable prose while retaining every mathematical expression verbatim."""
from pathlib import Path
import re
import subprocess
import shutil

ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / 'REMAINDER_FIRST_PROOF.tex').read_text()
aux = (ROOT / 'QA/BUILD/REMAINDER_FIRST_PROOF.aux').read_text()
labels = dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}', aux))
bib = dict(re.findall(r'\\bibcite\{([^}]+)\}\{([^}]+)\}', aux))
body = source.split(r'\begin{document}', 1)[1].split(r'\end{document}', 1)[0]
body = body.replace(r'\maketitle', '').replace(r'\tableofcontents', '')
body = re.sub(r'\\eqref\{([^}]+)\}', lambda m: '(' + labels[m[1]] + ')', body)
body = re.sub(r'\\ref\{([^}]+)\}', lambda m: labels[m[1]], body)
body = re.sub(r'\\label\{([^}]+)\}',
              lambda m: r'\tag{' + labels[m[1]] + '}' if m[1].startswith('eq:') else '', body)
body = re.sub(r'\\cite(?:\[([^\]]*)\])?\{([^}]+)\}',
              lambda m: '[' + ', '.join(bib[k] for k in m[2].split(','))
              + (', ' + m[1] if m[1] else '') + ']', body)

maths = []


def retain(m):
    token = 'MATHPLACEHOLDER' + str(len(maths)) + 'END'
    maths.append((token, m[0]))
    return token


body = re.sub(r'\\begin\{(equation\*?|align\*?|gather\*?)\}[\s\S]*?\\end\{\1\}', retain, body)
body = re.sub(r'\\\[[\s\S]*?\\\]', retain, body)
body = re.sub(r'(?<!\\)\$[^$]*?(?<!\\)\$', retain, body)

body = body.replace(r'\begin{abstract}', '\nAbstract\n').replace(r'\end{abstract}', '\n')
body = body.replace(r'\begin{proof}', '\nProof.\n').replace(r'\end{proof}', '\nEnd of proof.\n')
body = body.replace(r'\begin{thebibliography}{9}', '\nReferences\n').replace(r'\end{thebibliography}', '')
body = re.sub(r'\\bibitem\{([^}]+)\}', lambda m: '\n[' + bib[m[1]] + '] ', body)

# The optional theorem heading can contain nested provenance brackets.
statements = list(re.finditer(r'\\begin\{(theorem|lemma|proposition|remark)\}', body))
numbers = [labels[key] for key in re.findall(r'\\label\{((?:prop|lem|thm):[^}]+)\}', source)]
assert len(statements) == len(numbers)
for match, number in list(zip(statements, numbers))[::-1]:
    env = match[1]
    end = match.end()
    title = ''
    if body[end:end+1] == '[':
        depth, pos = 1, end + 1
        while depth:
            if body[pos] == '[':
                depth += 1
            elif body[pos] == ']':
                depth -= 1
            pos += 1
        title = body[end+1:pos-1]
        end = pos
    body = body[:match.start()] + '\n' + env.capitalize() + ' ' + number + (' (' + title + ')' if title else '') + '.\n' + body[end:]
body = re.sub(r'\\end\{(?:theorem|lemma|proposition|remark)\}', '\n', body)

section = 0


def heading(m):
    global section
    section += 1
    return '\n\n' + str(section) + '. ' + m[1] + '\n\n'


body = re.sub(r'\\section\{([^{}]+)\}', heading, body)
body = body.replace(r'\~n', 'ñ').replace('~', ' ')
detex = shutil.which('detex') or '/Library/TeX/texbin/detex'
text = subprocess.run([detex, '-l'], input=body, text=True,
                      check=True, capture_output=True).stdout
for token, expression in maths:
    assert text.count(token) == 1, token
    text = text.replace(token, expression)
text = re.sub(r'\n[ \t]*\n(?:[ \t]*\n)+', '\n\n', text)
header = '''FROM THE LIOUVILLE RESONANCE REMAINDER
TO ORDINARY TWO-POINT CANCELLATION

A remainder-first derivation from V. Casaña-Giner's decomposition
using intermediate estimates of the supplied OpenAI manuscript
7 November 2026

Plain-text edition. Mathematical expressions are retained in LaTeX notation.
The custom symbols are: \\N = natural numbers, \\Z = integers,
\\R = real numbers, \\T = R/Z, \\1 = indicator, \\E = expectation,
and \\ee(t) = exp(2 pi i t). All prose is in English.
Theorems and formulas have the same content as the accompanying TEX and PDF.

'''
out = header + text.strip() + '\n'
assert 'MATHPLACEHOLDER' not in out
assert '??' not in out
assert section == 8
(ROOT / 'REMAINDER_FIRST_PROOF.txt').write_text(out)
print(f'Exported {len(out)} characters with {len(maths)} preserved mathematical expressions.')
