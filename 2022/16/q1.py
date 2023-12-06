import heapq
import pprint
import re
import math
from collections import defaultdict


def main():
    with open("ex", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    valves = dict()
    for line in lines:
        src, fr, dst = re.findall(r"Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? (.*)", line)[0]
        valves[src] = {
            "fr": fr,
            "out": dst.split(", ")
        }

    # compute distances
    dist = defaultdict(lambda: defaultdict(lambda: math.inf))
    for v in valves:
        dist[v][v] = 0

    for _ in valves:
        for v in valves:
            for v2 in valves[v]["out"]:
                pass


if __name__ == '__main__':
    main()
