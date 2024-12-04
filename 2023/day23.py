from heapq import heappop, heappush

lookup = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}
FOUR_DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

with open("input.txt") as f:
    m = [[c for c in l.strip()] for l in f.readlines()]
    sx, sy = m[0].index("."), 0
    tx, ty = m[-1].index("."), len(m) - 1

    for part in [True, False]:
        graph = {(sx, sy): {}, (tx, ty): {}}
        q = [(0, sx, sy, (sx, sy), set())]

        while q:
            steps, x, y, start, cache = heappop(q)

            if steps > 0 and (x, y) in graph:
                graph[start][(x, y)] = steps
                continue

            if (x, y) in cache:
                continue
            cache.add((x, y))

            next = []
            for offx, offy in FOUR_DIRECTIONS:
                xx, yy = offx + x, offy + y
                if 0 <= xx < len(m[0]) and 0 <= yy < len(m) and m[yy][xx] != "#":
                    if part and m[y][x] in "^v<>":
                        tmp = lookup[m[y][x]]
                        if tmp[0] == offx and tmp[1] == offy:
                            next.append([xx,yy])
                    else:
                        next.append([xx,yy])

            if len(next) > 2:
                if (x, y) not in graph:
                    graph[(x, y)] = {}
                    graph[start][(x, y)] = steps
                for xx, yy in next:
                    heappush(q, ((1, xx, yy, (x,y), set())))
            else:
                for x, y in next:
                    heappush(q, (steps + 1, x, y, start, cache.copy()))

        q = [((sx, sy), 0, set())]
        maax = 0

        while q:
            edge, steps, c = q.pop()

            if edge in c:
                continue
            c.add(edge)

            if edge == (tx, ty):
                maax = max(maax, steps)
                continue

            for neighbour, step in graph[edge].items():
                if neighbour not in c:
                    s = c.copy()
                    q.append((neighbour, steps + step, s))

        print(maax)
