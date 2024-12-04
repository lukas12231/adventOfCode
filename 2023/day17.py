from heapq import *

def solve(m, is_part_2):
    DIRS = [(1,0), (0,1), (-1,0), (0,-1)]
    f = lambda x,y: [(x,y), DIRS[((DIRS.index((x,y)) + 1) % 4)], DIRS[((DIRS.index((x,y)) - 1) % 4)]]
    
    q = [(0, 0, 0, 1, 0, 0, 0)]
    cache = {}
    mx, my = len(m[0]), len(m)

    while q:
        heat ,x, y, dx, dy, straight, curve = heappop(q)

        key = (x, y, dx, dy, straight, curve)

        if key in cache and heat >= cache[key]:
            continue
        cache[key] = heat

        if x + 1 == mx and y + 1 == my:
            print(heat)
            return

        for offx, offy in f(dx, dy):
            nx, ny = offx + x, offy + y
            if nx >= 0 and nx < mx and ny >= 0 and ny < my:
                if offx == dx and offy == dy:
                    if (is_part_2 and straight < 10) or (not is_part_2 and straight < 3):
                        heappush(q, (heat + m[ny][nx], nx, ny, offx, offy, straight + 1, curve - 1 if curve > 0 else 0))
                elif curve == 0:
                    heappush(q, (heat + m[ny][nx], nx, ny, offx, offy, 1, 3 if is_part_2 else 0))

with open("input.txt") as f:
    m = [[int(c) for c in l.strip()] for l in f.readlines()]
    solve(m, False)
    solve(m, True)
