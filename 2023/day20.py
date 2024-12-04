import re
from math import lcm

with open("input.txt") as f:
    modules = {}
    brod = []
    for l in f.readlines():
        if "broadcaster" in l:
            brod = [c.strip() for c in l.split("->" )[1].split(",")]
            continue
        type, name, next = re.findall(r"([%&])(\w+) -> (.*)", l)[0]
        modules[name] = {
            "t": type,
            "next": [c.strip() for c in next.split(",")],
            "state": 0
        }
    for k, v in modules.items():
        if v["t"] == "&":
            modules[k]["input"] = {k2: 0 for k2,v2 in modules.items() if k in v2["next"]}

low, high = 0, 0

# part 2
# previous from rx is nr, this is a conjunction module --> all of them must be high to output a low signal
last = [k for k,_ in modules["nr"]["input"].items()]
cycles = [0 for _ in range(len(last))]

f = True
btn = 0
count = 0
while f:
    if count == 1000:
        print(low * high)
    count += 1
    messages = [(key, 0, "") for key in brod]
    low += len(brod) + 1
    btn += 1
    while messages:
        if all(v for v in cycles if v == 0):
            f = False
            break
        key, state, sender = messages.pop(0)
        if key == "rx":
            continue

        module = modules[key]

        if module["t"] == "%" and state == 0:
            modules[key]["state"] = 1 if module["state"] == 0 else 0
            for next in modules[key]["next"]:
                low += 1 if module["state"] == 0 else 0
                high += 1 if module["state"] == 1 else 0

                # part 2
                if key in last:
                    pos = last.index(key)
                    if module["state"] == 1 and cycles[pos] == 0:
                        cycles[pos] = btn

                messages.append((next, module["state"], key))

        if module["t"] == "&":
            modules[key]["input"][sender] = state
            out = 0
            if any(x == 0 for x in modules[key]["input"].values()):
                out = 1
            else:
                out = 0
            # part 2
            if out == 1 and key in last:
                pos = last.index(key)
                if cycles[pos] == 0:
                    cycles[pos] = btn

            for next in modules[key]["next"]:
                low += 1 if out == 0 else 0
                high += 1 if out == 1 else 0
                messages.append((next, out, key))

print(lcm(*cycles))
