from heapq import heappop, heappush
import numpy as np

def solve(start_x, start_y, m, steps):
    q = [(0, start_x, start_y)]
    positions = set()
    cache = set()
    check = (steps) % 2

    while q:
        step, x, y = heappop(q)
        
        if step % 2 == check:
            positions.add((x,y))

        if step == steps or (x,y) in cache:
            continue
        cache.add((x, y))

        for offx, offy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            xx = offx + x
            yy = offy + y
            if 0 <= xx < len(m[0]) and 0 <= yy < len(m) and m[yy][xx] in "S.":
                heappush(q, (step + 1, xx, yy))

    return len(positions)

with open("input.txt") as f:
    m = [l.strip() for l in f.readlines()]
    sx, sy = 0, 0
    for y, l in enumerate(m):
        for x, c in enumerate(l):
            if m[y][x] == "S":
                sx, sy = x, y
                break
    # part 1
    print(solve(sx, sy, m, 64))

    steps = 26501365

    # part 2
    # analizing the input data:
    # - start is in center of the garden
    # - a garden tile is a square
    # - middle lines do not contain any '#'
    # therfore, the expanding garden looks like a diamond

    out = 0

    steps = 26501365
    tile_len = len(m)
    amt = steps // tile_len
    rem = (steps - tile_len // 2 - 1) % tile_len

    # amount of full inside tiles in straight x and y direction
    odd_amt = (amt - 1 if amt % 2 == 0 else amt) ** 2
    even_amt = (amt - 1 if amt % 2 else amt) ** 2

    odd_gardens = solve(sx, sy, m, tile_len // 2 * 2 + 1)
    even_gardens = solve(sx, sy, m, tile_len // 2 * 2 + 2)

    out += odd_amt * odd_gardens + even_amt * even_gardens

    # corners
    corners = [solve(x,y,m,rem) for x,y in [(sx, tile_len - 1), (tile_len - 1, sy), (sx, 0), (0, sy)]]
    out += sum(corners)

    # edge cases
    small_amt = amt
    large_amt = amt - 1
    small_rem = rem - tile_len // 2 - 1
    large_rem = (rem - (tile_len // 2)) + tile_len - 1

    arr = [(0, tile_len - 1), (0,0), (tile_len - 1, 0), (tile_len - 1, tile_len - 1)]
    small = [solve(x,y,m,small_rem) for x,y in arr]
    large = [solve(x,y,m,large_rem) for x,y in arr]

    out += small_amt * sum(small) + large_amt * sum(large)

    print(out)


    #####################################################################################
    #                                                                                   #
    #  additional (found the idea on reddit, much easier method to calculate solution)  #
    #      https://www.reddit.com/r/adventofcode/comments/18nevo3/comment/keaidqr       #
    #                                                                                   #
    #####################################################################################
    big = []
    for line in range(5):
        for l in m:
            big.append("".join(5 * l))

    rem = steps % len(m)
    sx += 2 * len(m)
    sy += 2 * len(m)

    # to find a,b,c in ax^2 + bc + c --> 3 points are required
    # x = 0: 0 * garden_width + rest
    # x = 1: 1 * garden_width + rest
    # x = 2: 2 * garden_width + rest
    b = [solve(sx, sy, big, space) for space in [rem, rem + len(m), rem + 2 * len(m)]]
    A = np.array([[0, 0, 1], [1, 1, 1], [4, 2, 1]])
    x = np.linalg.solve(A, b)
    tiles = steps // len(m)
    a = np.array([tiles**2, tiles, 1])
    print(np.dot(a, x))
