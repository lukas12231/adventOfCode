# original
with open("input.txt") as f:
    m = [[c for c in l.split("\n")] for l in f.read().split("\n\n")]
    out, out2 = 0,0
    for elem in m:
        mrev = ["".join(x) for x in zip(*elem)]
        for multi, part in zip((100, 1), [elem, mrev]):
            for i in range(1, len(part)):
                first = [*reversed(part[:i])]
                second = part[i:]
                f = True
                t = 0
                for line in range(min(i, len(part) - i)):
                    # part 1
                    if first[line] != second[line]:
                        f = False
                    # part 2
                    for a, b in zip(first[line], second[line]):
                        t += 1 if a != b else 0
                if f:
                    out += i * multi
                if t == 1:
                    out2 += i * multi
    print(out, out2)

# just for fun :)
out, out2 = 0, 0
for elem in [[c for c in l.split("\n")] for l in open("input.txt").read().split("\n\n")]:
    for multi, part in zip((100, 1), [elem, ["".join(x) for x in zip(*elem)]]):
        for i in range(1, len(part)):
            first, second = [*reversed(part[:i])], part[i:]
            out += i * multi if not any([True for x in range(0, min(i, len(part) - i)) if first[x] != second[x]]) else 0
            out2 += i * multi if sum([1 for off in range(0, min(i, len(part) - i)) for a,b in zip(first[off], second[off]) if a != b]) == 1 else 0
print(out, out2)
