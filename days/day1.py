import re

with open("input.txt") as f:
    lines = f.readlines()
    
    # part 1
    solutions = [re.findall(r"\d", l) for l in lines]
    print(sum([int(f"{sol[0]}{sol[-1]}") for sol in solutions]))

    # part 2
    mapping = [str(x) for x in range(1,10)] + ["one","two","three","four","five","six","seven","eight","nine"]
    out = 0
    for l in lines:
        mi, ma = float("inf"),0
        results = []
        [[results.append((m.start(), t)) for m in re.finditer(t,l)] for t in mapping if t in l]
        results = [*map(lambda x: x[1], sorted(results, key=lambda x: x[0]))]
        f = lambda x: str(mapping.index(x) % 9 + 1)
        out += int(f"{f(results[0])}{f(results[-1])}")

    print(out)
