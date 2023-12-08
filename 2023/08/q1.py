import re


def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    instr = lines.pop(0)
    ptr = 0
    lines.pop(0)

    nodes = dict()
    for line in lines:
        info = re.findall(r"(\w+) = \((\w+), (\w+)\)", line)[0]
        nodes[info[0]] = tuple(info[1:])

    current_node = "AAA"
    steps = 0
    while current_node != "ZZZ":
        if instr[ptr] == "R":
            current_node = nodes[current_node][1]
        else:
            current_node = nodes[current_node][0]
        ptr = (ptr + 1) % len(instr)
        steps += 1

    print(steps)


if __name__ == '__main__':
    main()
