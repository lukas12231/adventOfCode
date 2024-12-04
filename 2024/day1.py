with open("input.txt") as f:
    a, b = list(zip(*[map(int, l.split()) for l in f.readlines()]))
    # task 1
    print(sum([abs(aa - bb) for aa, bb in zip(sorted(a), sorted(b))]))
    # task b
    print(sum([b.count(aa) * aa for aa in a]))
