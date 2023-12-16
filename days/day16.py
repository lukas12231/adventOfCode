from collections import deque

lookup = {
    "/": lambda x,y: [(-y, -x)],
    "\\": lambda x,y: [(y, x)],
    "-": lambda x,y: [(x, y)] if x else [(-1,0),(1,0)],
    "|": lambda x,y: [(x, y)] if y else [(0,-1),(0,1)],
    ".": lambda x,y: [(x, y)]
}

with open("input.txt") as f:
    m = [[c for c in l.strip()] for l in f.readlines()]
    mx = len(m[0])
    my = len(m)

    mout = 0
    first = True
    for y in range(my):
        for x in range(mx):
            for xx, yy in [(1,0), (0,1), (-1,0), (0,-1)]:
                cache, cache2 = set(), set()
                q = deque([((x, y), (xx, yy))])
                while q:
                    key = q.popleft()
                    (x, y), (dirx, diry) = key
                    if x < 0 or x >= mx or y < 0 or y >= my or key in cache:
                        continue

                    cache.add(key)
                    cache2.add((x,y))

                    c = m[y][x]
                    for xx, yy in lookup[c](dirx, diry):
                        nx = x + xx
                        ny = y + yy
                        q.append(((nx, ny), (xx, yy)))
                if first:
                    print(len(cache2))
                    first =False
                mout = max(mout, len(cache2))
    print(mout)
