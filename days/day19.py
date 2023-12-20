import re

with open("input.txt") as f:
    tmp = f.read()
    wf = tmp.split("\n\n")[0]
    # evals is for part1, evals2 added for part2
    evals, evals2 = {}, {}

    for l in wf.splitlines():
        name = l.split("{")[0]
        test = re.findall(r"([xmas][<>]\d+):(\w+)", l)
        rem = l.split(",")[-1][:-1]
        evals[name] = [(logic[0], eval(f"lambda {logic[0]}: '{out}' if {logic} else None")) for logic, out in test]
        evals[name].append(rem)
        evals2[name] = [(logic, out) for logic, out in test]
        evals2[name].append(rem)

    p = []
    for parts in tmp.split("\n\n")[1].splitlines():
        s = [(x, int(y)) for x, y in re.findall(r"(\w+)=(\d+)", parts)]
        p.append(s)

    # original part 1
    output = 0
    for test in p:
        pos = "in"
        while True:
            for testname, check in evals[pos][:-1]:
                for name, val in test:
                    if name == testname:
                        out = check(val)
                        if out:
                            pos = out
                            break
                if out:
                    pos = out
                    break
            if not out:
                pos = evals[pos][-1]
            if pos == "A":
                output += sum([x[1] for x in test])
                break
            if pos == "R":
                break
    print(output)

    # part 2
    q = [[1, 4000, 1, 4000, 1, 4000, 1, 4000, "in"]]
    out = 0

    while q:
        elem = q.pop(0)
        p = elem[-1]
        if p == "A":
            tmp = 1
            for i in range(4):
                tmp *= elem[i*2 + 1] - elem[i*2] + 1
            out += tmp
            continue
        if p == "R":
            continue

        for test, name in evals2[p][:-1]:
            check_elem = re.findall(r"\w+", test)[0]
            border = int(re.findall(r"\d+", test)[0])

            idx = "xmas".index(check_elem)
            lower, upper = elem[idx*2], elem[idx*2+1]

            if ">" in test:
                next = (border + 1, upper)
                rem = (lower, border)

            if "<" in test:
                next = (lower, border - 1)
                rem = (border, upper)

            if next[0] <= next[1]:
                elem[idx*2] = next[0]
                elem[idx*2 + 1] = next[1]
                elem[-1] = name
                q.append(elem[:])

            if rem[0] <= rem[1]:
                elem[idx*2] = rem[0]
                elem[idx*2 + 1 ] = rem[1]
            else:
                break
        elem[-1] = evals2[p][-1]
        q.append(elem[:])

    print(out)
