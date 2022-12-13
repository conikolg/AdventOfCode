import functools


def load_file(filename):
    with open(filename, "r") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


def main(lines):
    packets = [
        [[2]],
        [[6]]
    ]
    while len(lines) > 0:
        first = eval(lines.pop(0))
        second = eval(lines.pop(0))
        packets.append(first)
        packets.append(second)
        lines.pop(0)

    def sort_compare(x, y):
        c = compare(x, y)
        if c is None:
            return 0
        else:
            return -int(c)

    packets = sorted(packets, key=functools.cmp_to_key(sort_compare))

    for pkt in packets:
        print(pkt)

    i = packets.index([[2]])
    j = packets.index([[6]])
    print(i, j)
    print((i + 1) * (j + 1))


def compare(x, y):
    # print(f"comparing {x=} {y=}")
    if isinstance(x, int) and isinstance(y, int):
        if x < y:
            return True
        if x == y:
            return None
        return False

    if isinstance(x, list) and isinstance(y, list):
        for i in range(len(x)):
            try:
                c = compare(x[i], y[i])
                if c == True:
                    return True
                if c == False:
                    return False
            except:  # y ran out
                return False
        # Exhausted both evenly
        if len(x) == len(y):
            return None
        # x ran out
        return True

    if isinstance(x, int):
        x = [x]
    if isinstance(y, int):
        y = [y]

    return compare(x, y)


if __name__ == '__main__':
    main(load_file(filename="in"))
