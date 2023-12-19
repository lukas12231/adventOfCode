lookup = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0), 0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}

def polygonArea(vertices):
    # found here: https://www.101computing.net/the-shoelace-algorithm/
    numberOfVertices = len(vertices)
    sum1 = 0
    sum2 = 0
    for i in range(0, numberOfVertices - 1):
        sum1 = sum1 + vertices[i][0] * vertices[i + 1][1]
        sum2 = sum2 + vertices[i][1] * vertices[i + 1][0]
    # Add xn.y1
    sum1 = sum1 + vertices[numberOfVertices - 1][0] * vertices[0][1]
    # Add x1.yn
    sum2 = sum2 + vertices[0][0] * vertices[numberOfVertices - 1][1]

    area = abs(sum1 - sum2) / 2
    return area

def circumference(poly):
    return sum([ abs(poly[id][j] - poly[id - 1][j]) for id in range(1, len(poly)) for j in range(2)])

with open("input.txt") as f:
    m = []
    for l in f.readlines():
        tmp = l.split(" (")[0].split(" ")
        p2 = l.split("#")[1].strip()[:-1]
        m.append(((tmp[0], int(tmp[1])), (int(p2[-1]), int(p2[:-1], 16))))

    out = [(0, 0)]
    for i in range(2):
        x, y = 0, 0
        out = [(0, 0)]
        for dig in m:
            dir, amt = dig[i]
            offx, offy = lookup[dir]
            x = x + amt * offx
            y = y + amt * offy
            out.append((x, y))

        print(int(polygonArea(out) + circumference(out) // 2 + 1))
