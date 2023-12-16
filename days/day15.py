import re

with open("input.txt") as f:
    i = f.read().split(",")
    out, out2 = 0, 0

    # part 1
    for el in i:
        tmp = 0
        for c in el:
            tmp = (tmp + ord(c)) * 17 % 256
        out += tmp

    # part 2
    boxes = {
        i: {} for i in range(256)
    }

    for el in i:
        label = re.findall(r"([a-z])", el)
        hash = 0
        for c in label:
            hash = (hash + ord(c)) * 17 % 256
        label = "".join(label)
        if "-" in el and label in boxes[hash]:
            del boxes[hash][label]
        if "=" in el:
            boxes[hash][label] = re.findall(r"\d+", el)[0]

    for i, box in boxes.items():
        for j, v in enumerate(box.values()):
            out2 += (i + 1) * (j + 1) * int(v)
    print(out, out2)
