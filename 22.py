import re

def neighbour(i, up: bool):
    tmp = set()
    off = 1 if up else -1
    for x, y, z in blocks[i]:
        if (x, y, z + off) in blocks2 and blocks2[(x, y, z + off)] != i:
            tmp.add(blocks2[(x, y, z + off)])
    return tmp

def removable(i):
    for j in neighbour(i, True):
        under = neighbour(j, False)
        if len(under) < 2:
            return False
    return True

with open("input.txt") as f:
    coords = [[*map(int, re.findall(r"\d+", l))] for l in f.readlines()]
    coords.sort(key=lambda x: x[2])
    blocks, blocks2 = {}, {}

    for i, (x, y, z, xe, ye, ze) in enumerate(coords):
        run = True
        blocks[i] = []
        while run:
            for xx in range(x, xe + 1):
                for yy in range(y, ye + 1):
                    for zz in range(z, ze + 1):
                        if (xx, yy, zz - 1) in blocks2 or z - 1 < 0:
                            run = False
            if run:
                z -= 1
                ze -= 1
        for xx in range(x, xe + 1):
            for yy in range(y, ye + 1):
                for zz in range(z, ze + 1):
                    blocks[i].append((xx, yy, zz))
                    blocks2[(xx, yy, zz)] = i

    # part 1
    print(sum(1 for block in blocks.keys() if removable(block)))

    # part 2
    fall_count, over, under = {}, {}, {}
    maxZ = max(k[2] for k in blocks2.keys())

    for z in reversed(range(maxZ + 1)):
        tmp = set([value for key, value in blocks2.items() if key[2] == z])

        for elem in tmp:
            if elem not in fall_count:
                # top element
                over[elem] = neighbour(elem, True)
                under[elem] = neighbour(elem, False)

                if not removable(elem):
                    fall = 0
                    q = list(over[elem])
                    c = {elem}
                    while q:
                        e = q.pop(0)

                        if not all(y in c for y in under[e]):
                            continue

                        if e in c:
                            continue
                        c.add(e)

                        fall += 1
                        for x in over[e]:
                            q.append(x)

                    fall_count[elem] = fall
    print(sum(fall_count.values()))
