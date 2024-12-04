import re 
from functools import cache
import itertools

@cache
def check(line, numbers: tuple, pos_line: int, state: bool):
    if sum(numbers) == 0:
        return 0 if "#" in line[pos_line:] else 1

    if pos_line == len(line):
        return 1 if sum(numbers) == 0 else 0
    
    c = line[pos_line]
    curr_num = numbers[0]

    if c == ".":
        if state:
            if curr_num == 0:
                return check(line, numbers[1:], pos_line + 1, False)
            return 0
        return check(line, numbers, pos_line + 1, False)

    if c == "#":
        if state and numbers[0] == 0:
            return 0
        return check(line, (numbers[0] - 1, *numbers[1:]), pos_line + 1, True)

    if c == "?":
        if state:
            if curr_num == 0:
                return check(line, numbers[1:], pos_line + 1, False)
            return check(line, (numbers[0] - 1, *numbers[1:]), pos_line + 1, True)
        return check(line, numbers, pos_line + 1, False) + check(line, (numbers[0] - 1, *numbers[1:]), pos_line + 1, True)

with open("input.txt") as f:
    lines = f.readlines()
    m = ["".join([x for x in l if x in "#.?"]) for l in lines]
    num = [tuple(map(int, re.findall(r"\d+", l))) for l in lines]

    o = 0
    o2 = 0
    # part 1 and 2
    for num, line in zip(num, m):
        o += check(line, num, 0, False)
        o2 += check("?".join([line for _ in range(5)]), 5 * num, 0, False)
    print(o, o2)


# first stupid method for part 1, needs ~60sek
with open("input.txt") as f:
    out = 0
    all = f.readlines()
    m = ["".join([c for c in y if c in ["#", ".", "?"]]) for y in all]
    nrs = [[int(x) for x in re.findall(r"\d+", y)] for y in all]

    for i, l in enumerate(m):
        amt = l.count("?")
        group = nrs[i]
        for outp in itertools.product([".", "#"], repeat=amt):
            checker = l[:]
            for tmp in outp:
                ii = checker.index("?")
                checker = checker[:ii] + tmp + checker[ii + 1:]
            
            grps = checker.split(".")
            val = [len(x) for x in grps if len(x) > 0]

            if len(val) == len(group) and not any([True for x,y in zip(val, group) if x != y]):
                out += 1

    print(out)
