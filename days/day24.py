import re

import numpy as np
from sympy import Matrix, Symbol, solve

with open("input.txt") as f:
    hail = []
    for l in f.readlines():
        a = re.findall(r"(-?\d+)", l)
        hail.append(tuple([*map(int,a)]))

    cross = 0
    # part 1
    for i,a in enumerate(hail):
        for b in hail[i+1:]:

            A = np.array([[a[3], -b[3]], [a[4], -b[4]]])
            bb = np.array([b[0] - a[0], b[1] - a[1]])
            try:
                out = np.linalg.solve(A,bb)
            except:
                continue
            
            x = out[0] * a[3] + a[0]
            y = out[0] * a[4] + a[1]

            if all(False for o in out if o < 0):
                if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000:
                    cross += 1
    print(cross)
    # part 2 - solve non linear equation system with sympy

    # rock       = t * v_0 + s_0
    # hailstones = t[i] * v_i + s_i

    # s_0 + t[i] * v_0 = s_i + t[i] * v_i
    # 0 = s_i + t[i] * v_i - s_0 - t[i] * v_0
    # 0 = s_i - s_0 + t[i] * (v_i - v_0)

    s = [Symbol("sx"), Symbol("sy"), Symbol("sz")]
    v = [Symbol("vx"), Symbol("vy"), Symbol("vz")]
    t = [Symbol("t1"), Symbol("t2"), Symbol("t3")]

    equations = []
    for i, h in enumerate(hail[:3]):
        for j in range(3):
            equations.append(h[j] - s[j] + t[i] * (h[j + 3] - v[j]))
    r = solve(equations, *s, *v, *t)
    print(sum(r[0][:3]))


    # alternative: solve as a linear equation system
    # idea: Rock: r(t) = s_0 + t * v_0
    #       Hail: h(t_i) = s_i + t_i * v_i
    # r(t) = h(t_i)
    # s_0 - s_i = t_i * (v_i - v_0) --> (s_0 - s_i) is parallel to (v_i - v_0) --> cross product is 0
    # (I) (s_0 - s_i) x (v_i - v_0) = 0
    # s_0 x v_i - s_0 x v_0 - s_i x v_i + s_i x v_0 = 0
    # I(P_j) = I(P_i) --> removes non linear component s_0 x v_0
    # use 2 different combinations of points to create 6 Equations (v_i and v_j must be linear independend)

    A = np.array([[hail[0][0]] * 6] * 6)
    b = np.array([0.0] * 6)
    # i use point 0, 2 and 3, because with 0, 1 and 2 i have rounding errors
    for idx, (i, j) in enumerate([(0,2), (0,3)]):
        pi, vi, pj, vj = hail[i][:3], hail[i][3:], hail[j][:3], hail[j][3:]

        A[idx * 3]     = [ vi[1] - vj[1], -(vi[0] - vj[0]), 0, -(pi[1] - pj[1]), pi[0] - pj[0], 0 ]
        A[idx * 3 + 1] = [ 0, vi[2] - vj[2], -(vi[1] - vj[1]), 0, -(pi[2] - pj[2]), pi[1] - pj[1] ]
        A[idx * 3 + 2] = [ -(vi[2] - vj[2]), 0, vi[0] - vj[0], pi[2] - pj[2], 0, -(pi[0] - pj[0]) ]

        b[idx * 3]     = pi[0] * vi[1] - vi[0] * pi[1] - pj[0] * vj[1] + vj[0] * pj[1]
        b[idx * 3 + 1] = pi[1] * vi[2] - vi[1] * pi[2] - pj[1] * vj[2] + vj[1] * pj[2]
        b[idx * 3 + 2] = pi[2] * vi[0] - vi[2] * pi[0] - pj[2] * vj[0] + vj[2] * pj[0]
    res = np.linalg.solve(A,b)

    print(int(sum(res[:3])))
