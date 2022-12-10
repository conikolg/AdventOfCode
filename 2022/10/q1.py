def load_file(filename):
    with open(filename, "r") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


def main(lines):
    cycle = 1
    x = 1
    signal_sum = 0
    for line in lines:
        if cycle in [20, 60, 100, 140, 180, 220]:
            signal_sum += x * cycle
        cycle += 1

        if line.startswith("noop"):
            pass
        else:
            if cycle in [20, 60, 100, 140, 180, 220]:
                signal_sum += x * cycle
            cycle += 1
            v = int(line.split()[1])
            x += v

    while cycle < 225:
        if cycle in [20, 60, 100, 140, 180, 220]:
            signal_sum += x * cycle
        cycle += 1

    print(signal_sum)


if __name__ == '__main__':
    main(load_file(filename="in"))
