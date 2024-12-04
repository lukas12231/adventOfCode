out, out2 = 0,0
with open("input.txt") as f:
    m = f.readlines()

    rev = list(zip(*m))
    rows = [x for x,c in enumerate(m) if "#" not in c]
    cols = [x for x,c in enumerate(rev) if "#" not in c]

    coords = [(x, y) for y, l in enumerate(m) for x,c in enumerate(l) if c == "#"]

    for i, (x1, y1) in enumerate(coords[:-1]):
        for (x2, y2) in coords[i + 1:]:
            xa = min(x1, x2)
            xe = max(x1, x2)

            ya = min(y1, y2)
            ye = max(y1, y2)

            r = len([y for y in rows if y >= ya and y <= ye])
            cc = len([y for y in cols if y >= xa and y <= xe])

            out += xe - xa + ye - ya + r * 1000000 + cc * 1000000 - r - cc
    print(out)
