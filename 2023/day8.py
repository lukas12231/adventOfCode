import math
import re

with open("input.txt") as f:
    l = f.readlines()
    instruc = [c for c in l[0].strip()]
    tmp = {a[0] : a[1:] for a in [tuple(re.findall(r"\w+", x)) for x in l[2:]]}

    # part 1
    start = "AAA"
    s = 0
    i = instruc[0]
    while start != "ZZZ":
        start = tmp[start][0] if instruc[s % len(instruc)] == "L" else tmp[start][1]
        s += 1
    print(s)

    # part 2
    s = 0
    start = [a for a in tmp.keys() if a.endswith("A")]
    # 0 - steps to reach z for first time
    # 1 - steps to reach z for second time
    cycles = [[0,0] for _ in range(len(start))]

    while any([True for x in cycles if x[1] == 0]):
        for i,x in enumerate(start):
            start[i] = tmp[start[i]][0] if instruc[s % len(instruc)] == "L" else tmp[start[i]][1]
            if start[i].endswith("Z"):
                if cycles[i][0] == 0:
                    cycles[i][0] = s + 1
                else:
                    cycles[i][1] = s + 1 - cycles[i][0]
        s += 1
    # check if the amount of steps to reach target for first time is equal to the amount of steps to 
    # reach the target again
    if any([True for x, y in cycles if x != y]):
        out = math.lcm(*[x for x,y in cycles])
        print(out)
