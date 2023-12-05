import math
import re

with open("input.txt") as f:
    g = lambda x: [*map(int, re.findall(r"\d+", x))]
    l = [[*map(g, (x.split(":")[1].split("|")[0].strip(), x.split("|")[1].strip()))] for x in f.readlines()]
    out = 0
    amt = [1 for _ in range(len(l))]

    for id, x in enumerate(l):
        win, test = x
        matches = len([1 for nr in win if nr in test])
        o = math.floor(2 ** (matches - 1))
        val = amt[id]
        for x in range(id + 1, id + matches + 1):
            amt[x] += val
        out += o

print(out, sum(amt))
