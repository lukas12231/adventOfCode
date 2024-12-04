import re

with open("input.txt") as f:
    l = f.readlines()
    # task 1
    times = [*map(int, re.findall(r"\d+", l[0]))]
    d = [*map(int,re.findall(r"\d+", l[1]))]

    out = 1
    for t, dist in zip(times, d):
        o = 0
        for x in range(1, t):
            amt = (t - x) * x
            if amt > dist:
                o+=1
        out *= o
    print(out)

    # task 2
    out = 0
    time = int("".join([*map(str,times)]))
    d = int("".join([*map(str,d)]))

    for x in range(1, time):
        amt = (time-x) * x
        if amt > d:
            out+=1
    print(out)
