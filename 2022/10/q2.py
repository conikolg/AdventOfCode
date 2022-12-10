def load_file(filename):
    with open(filename, "r") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


def main(lines):
    # slightly flawed - it applies all adds one cycle too early.
    # seems that all this does though is shift the real left-most column to the right side of the output

    x = 1
    line = 0
    wait = 0

    for cycle in range(1, 241):
        if cycle in [41, 81, 121, 161, 201]:
            print("")
        print("#" if abs(cycle % 40 - x) < 2 else " ", end="")
        if wait == 1:
            wait = 0
        else:
            if lines[line].startswith("noop"):
                pass
            else:
                x += int(lines[line].split()[1])
                wait = 1
            line += 1


if __name__ == '__main__':
    main(load_file(filename="ex"))
