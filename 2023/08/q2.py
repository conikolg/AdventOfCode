import math
import pprint
import re
from collections import defaultdict


def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    instr = lines.pop(0)
    lines.pop(0)

    nodes = dict()
    for line in lines:
        info = re.findall(r"(\w+) = \((\w+), (\w+)\)", line)[0]
        nodes[info[0]] = tuple(info[1:])

    current_nodes = [n for n in nodes.keys() if n.endswith("A")]

    stats = defaultdict(lambda: dict())
    for n in current_nodes:
        start = n
        steps = 0
        while not n.endswith("Z"):
            if instr[steps % len(instr)] == "R":
                n = nodes[n][1]
            else:
                n = nodes[n][0]
            steps += 1
        stats[start]["first"] = steps

        # Go again
        if instr[steps % len(instr)] == "R":
            n = nodes[n][1]
        else:
            n = nodes[n][0]
        steps += 1
        while not n.endswith("Z"):
            if instr[steps % len(instr)] == "R":
                n = nodes[n][1]
            else:
                n = nodes[n][0]
            steps += 1

        stats[start]["repeat"] = steps - stats[start]["first"]

    pprint.pprint(stats)

    # they go in their own loops
    print(math.lcm(*[f["first"] for f in stats.values()]))


if __name__ == '__main__':
    main()
