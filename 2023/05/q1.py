import utils


def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    x: [int] = utils.int_split(lines.pop(0).split(":")[1])
    lines.pop(0)

    while len(lines) > 0:
        # map title
        try:
            lines.pop(0)
        except Exception:
            break

        Map = []
        while True:
            try:
                line = lines.pop(0)
            except Exception:
                break
            if len(line) == 0:
                break

            info = utils.int_split(line)
            Map.append((info[1], info[2], info[0]))

        for i in range(len(x)):
            x[i] = convert(x[i], Map)

    print(min(x))


def convert(x, maps):
    for m in maps:
        diff = x - m[0]
        if diff < 0 or diff >= m[1]:
            continue

        return m[2] + diff

    return x


if __name__ == '__main__':
    main()
