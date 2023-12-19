import utils


def tilt_north(lines: [[str]]):
    for j in range(len(lines[0])):
        column = "".join(lines[i][j] for i in range(len(lines)))
        parts: [str] = column.split("#")
        for i, p in enumerate(parts):
            parts[i] = "".join(sorted(p, reverse=True))
        column = "#".join(parts)
        for i in range(len(lines)):
            lines[i][j] = column[i]


def cycle(lines: [[str]]):
    for i in range(4):
        tilt_north(lines)
        lines = utils.rotate_cw(lines)
    return lines


def pressure(lines: [[str]]):
    answer = 0
    for i in range(len(lines)):
        points = len(lines) - i
        answer += points * "".join(lines[i]).count("O")
    return answer


def flat(lines: [[str]]):
    return "".join(["".join(line) for line in lines]), len(lines[0])


def main():
    with open("in.txt", "r") as infile:
        lines = [list(line.strip()) for line in infile.readlines()]

    stages = [flat(lines)]
    cycles = 0
    repeat = None
    while True:
        lines = cycle(lines)
        cycles += 1
        if flat(lines) in stages:
            repeat = len(stages) - stages.index(flat(lines))
            break
        else:
            stages.append(flat(lines))

    remaining = (1000000000 - cycles) % repeat
    for _ in range(remaining):
        lines = cycle(lines)

    print(len(stages), cycles, repeat)
    print(pressure(lines))


if __name__ == '__main__':
    main()
