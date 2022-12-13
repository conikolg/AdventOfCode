def load_file(filename):
    with open(filename, "r") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


def main(lines):
    index = 1
    total = 0
    while len(lines) > 0:
        first = eval(lines.pop(0))
        second = eval(lines.pop(0))
        lines.pop(0)

        print(f"testing {first=} {second=}")
        c = compare(first, second)
        if c == False:
            print("Bad")
        else:
            print("Good")
            total += index

        print("")
        index += 1

    print(total)


def compare(x, y):
    print(f"comparing {x=} {y=}")
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
