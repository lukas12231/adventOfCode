import re

import networkx

# minimum cut problem, see https://en.wikipedia.org/wiki/Minimum_cut --> Stoer Wagner Algorithm, found in networkx
with open("input.txt") as f:
    g = networkx.Graph()
    for l in f.readlines():
        t = re.findall(r"\w+", l)
        for c in t[1:]:
            g.add_edge(t[0], c, weight=1.0)

cut_val, partitions = networkx.stoer_wagner(g)
print(len(partitions[0]) * len(partitions[1]))
