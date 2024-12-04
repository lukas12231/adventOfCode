dic = {}

directions = {
    "|": [(0, 1), (0, -1)],
    "-": [(1, 0), (-1, 0)],
    "L": [(0, -1), (1, 0)],
    "J": [(-1, 0), (0, -1)],
    "7": [(-1, 0), (0, 1)],
    "F": [(1, 0), (0, 1)],
}

with open("input.txt") as f:
    m = [[x for x in y.strip()] for y in f.readlines()]
    # find start
    for y, l in enumerate(m):
        for x, c in enumerate(l):
            if c == "S":
                start = (y, x)
                # after checking input file, start must be a "|"
                m[y][x] = "|"

    # part 1
    q = [(start, [(1,0), (0,1), (-1,0), (0,-1)], 0)]
    while q:
        coords, off, long = q.pop(0)
        x, y = coords

        for offx, offy in off:
            tx, ty = x + offx, y + offy
            if tx >= 0 and tx < len(m[0]) and ty >= 0 and ty < len(m):
                next = m[ty][tx]

                for k, v in directions.items():
                    # if next is suitable from discovery direction
                    if k == next and (-1 * offx, -1 * offy) in v:
                        key = f"{x}-{y}"
                        if key not in dic:
                            dic[key] = set()
                        if (tx, ty) not in dic[key]:
                            q.append([(tx, ty), v, long + 1])
                        dic[key].add((tx, ty))

    print(len(dic.keys()) // 2)

    # part 2
    # use the idea how to check if a poin is in a polygon or not 
    # (count intersections of borders in a horizontal line from left to checked point) -> amount must be odd number
    # a border can be: 
    #   "|"
    #   "F", followed by "J" (between them, "-" are possible) 
    #   "L", followed by "7"
    inside = 0
    for y, l in enumerate(m):
        for x, c in enumerate(l):
            if f"{x}-{y}" not in dic:
                intersections = 0
                last = None
                for xx in range(x):
                    if f"{xx}-{y}" in dic:
                        test = m[y][xx]
                        if test == "|":
                            intersections += 1
                            last = None
                        if test == "J" and last == "F":
                            intersections += 1
                            last = None
                        if test == "7" and last == "L":
                            intersections += 1
                            last = None
                        if test in ["F", "L"]:
                            last = test
                if intersections % 2 == 1:
                    inside += 1
    print(inside)
