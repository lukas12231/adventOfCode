def slide(rocks):
    rev = ["".join(x) for x in zip(*rocks)]
    split = [l.split("#") for l in rev]
    rocks = ["#".join(reversed(["".join(sorted(segment)) for segment in l])) for l in split]
    return rocks

with open("input.txt") as f:
    rocks = [l.strip() for l in f.readlines()]

    # part 1
    # rocks = rotate(rocks)
    # points = sum([idx + 1 for l in rocks for idx, c in enumerate(l) if c == "O"])

    # part 2
    lookup = {}
    cache = []
    for i in range(1000000000):
        key = "".join(rocks)
        if key in lookup:
            break
        rev = ["".join(reversed(x)) for x in zip(*rocks)]
        lookup[key] = sum([idx + 1 for l in rev for idx, c in enumerate(l) if c == "O"])
        cache.append(key)
        for _ in range(4):
            rocks = slide(rocks)

    off = cache.index(key)
    cycle = i - off
    tmp = cache[((1000000000 - off) % cycle) + off]
    out = lookup[tmp]
    print(out)
