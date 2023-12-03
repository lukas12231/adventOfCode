import re
import numpy

# part 1
with open("input.txt") as f:
    out = 0
    colors = ["red", "green", "blue"]
    for l in f.readlines():
        valid = True
        sets = re.findall(r"(\d+) (\w+)", l)
        if any(int(amt) > 12 + colors.index(color) for amt, color in sets):
            continue
        out += int(re.findall(r"\d+", l)[0])
    print(out)

# part 2
with open("input.txt") as f:
    out = 0
    colors = ["red", "green", "blue"]
    for l in f.readlines():
        valid = True
        sets = re.findall(r"(\d+) (\w+)", l)
        maxis = {}
        for amt, color in sets:
            maxis[color] = max(maxis.get(color, 0), int(amt))
        out += numpy.prod([val for val in maxis.values()])
    print(out)