import re
import numpy

out = 0
out2 = 0
gears = {}

with open("input.txt") as f:
    m = [x.strip() for x in f.readlines()]
    
for y, line in enumerate(m):
    posi = [(x.start(), x.end(), x.group(0)) for x in re.finditer(r"\d+", line)]

    for idx, pos in enumerate(posi):
        st, end, val = pos
        f = False
        for x in range(st, end):
            for xx in range(x-1, x+2):
                for yy in range(y-1, y+2):
                    if yy >= 0 and yy < len(m) and xx >= 0 and xx < len(m[yy]):
                        if m[yy][xx] != "." and not m[yy][xx].isnumeric():
                            f = True
                        if m[yy][xx] == "*":
                            key = f"{yy}{xx}"
                            if key not in gears:
                                gears[key] = set()
                            gears[key].add(int(val))
        if f:
            out += int(val)

for gear in gears.values():
    if len(list(gear)) == 2:
        out2 += numpy.prod(list(gear))

print(out, out2)
