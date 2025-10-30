s, t = open("Data/_10_1.txt").read().splitlines(), dict(
    zip("|-LJ7FS.", (16644, 1344, 1284, 324, 16704, 17664, 17988, 0))
)
g, n = [
    (t[c] >> i + j) & 3 for r in s for i in (0, 6, 12) for c in r for j in (0, 2, 4)
], 3 * len(s)
import operator as o


def f(s, v=0):
    return len(
        [
            o.setitem(g, p, s.append(p) or 2)
            for q in s
            for p in (q - n, q + n, q + 1, q - 1)
            if v <= g[p] < 2
        ]
    )


print(
    (f([g.index(2)], 1) - 1) // 6,
    f([0])
    and n * n // 9
    - sum(g[n * i + 1 : n * i + n + 1 : 3].count(2) for i in range(1, n, 3)),
)
