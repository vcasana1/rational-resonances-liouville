"""Finite checks of exact identities; not asymptotic proof validation."""
from collections import defaultdict
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from math import gcd
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent


def floor(x):
    return int(x.to_integral_value(rounding=ROUND_FLOOR))


def ceiling(x):
    return int(x.to_integral_value(rounding=ROUND_CEILING))


def liouville(n):
    assert n >= 1
    sign = 1
    d = 2
    while d * d <= n:
        while n % d == 0:
            sign = -sign
            n //= d
        d += 1
    return -sign if n > 1 else sign


def S(j, t):
    return sum(liouville(n) * liouville(n - j)
               for n in range(j + 1, max(j + 1, floor(t) + 1)))


with localcontext() as ctx:
    ctx.prec = 80
    block_cases = block_terms = band_cases = negative_one_cases = 0
    endpoint_max = {}
    for p in range(1, 6):
        for q in range(1, 6):
            if gcd(p, q) != 1:
                continue
            for X in [1, 2, 7, 31, 100, 251]:
                for c_text in ['-4', '-2', '-1', '-0.5', '0', '0.5', '1', '2', '3.2']:
                    c = Decimal(c_text)
                    e = (c / X).exp()
                    slope = Decimal(p) / q * e
                    delta = Decimal(p) / q * (e - 1)
                    direct = 0
                    blocks = defaultdict(int)
                    for n in range(1, X + 1):
                        a, k = n % q, n // q
                        b = (p * a) // q
                        s = p * a - q * b
                        r = floor(Decimal(s) / q + delta * n)
                        target = (p * n) // q if c == 0 else floor(slope * n)
                        assert target == p * k + b + r, (p, q, X, c_text, n, target, k, b, r)
                        if target < 1:
                            continue
                        term = liouville(n) * liouville(target)
                        direct += term
                        blocks[a, r] += term
                        if (a, r) != (0, 0):
                            d0 = min(p * a, q * (b + r))
                            h = abs(q * (b + r) - p * a)
                            assert h > 0
                            m = p * q * k + d0
                            assert m >= 1
                            assert term == liouville(p * q) * liouville(m) * liouville(m + h)
                            block_terms += 1
                    main_count = sum(floor(Decimal(p) * e * k) == p * k
                                     for k in range(1, X // q + 1))
                    remainder = sum(v for key, v in blocks.items() if key != (0, 0))
                    assert direct == liouville(p * q) * main_count + remainder
                    if c > 0:
                        count_formula = min(X // q, ceiling(1 / (p * (e - 1))) - 1)
                        assert main_count == count_formula
                    elif c < 0:
                        assert main_count == 0
                    else:
                        assert main_count == X // q
                    block_cases += 1

    for h in range(1, 9):
        max_error = 0
        for X in [100, 151, 251, 500, 1000]:
            alpha = 1 - (-Decimal(h) / X).exp()
            assert ceiling(alpha * X) == h
            direct = sum(liouville(n) * liouville(target)
                         for n in range(1, X + 1)
                         if (target := floor((1 - alpha) * n)) >= 1)
            exact = sum(S(j, min(Decimal(X), Decimal(j) / alpha))
                        - S(j, Decimal(j - 1) / alpha)
                        for j in range(1, h + 1))
            assert direct == exact
            limiting_bands = sum(S(j, Decimal(j * X) / h)
                                 - S(j, Decimal((j - 1) * X) / h)
                                 for j in range(1, h + 1))
            max_error = max(max_error, abs(exact - limiting_bands))
            band_cases += 1
        endpoint_max[str(h)] = max_error

    for X in range(1, 401):
        slope = (-Decimal(1) / X).exp()
        assert all(floor(slope * n) == n - 1 for n in range(1, X + 1))
        negative_one_cases += 1

result = {
    'status': 'passed',
    'decimal_precision': 80,
    'block_decomposition_cases': block_cases,
    'nonproportional_conversion_terms': block_terms,
    'exact_negative_band_cases': band_cases,
    'exact_negative_one_cases': negative_one_cases,
    'observed_limiting_band_error_by_shift': endpoint_max,
    'scope': 'Finite checks of identities only. These checks do not verify the external graph inputs or prove any asymptotic cancellation.'
}
(ROOT / 'EXACT_IDENTITY_CHECKS.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
