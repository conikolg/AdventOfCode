import itertools


def reflection(p: [str]):
    for i in range(len(p) - 1):
        if p[i] == p[i + 1]:
            offset = 0
            while True:
                try:
                    if i - offset < 0:
                        raise IndexError
                    if p[i - offset] != p[i + 1 + offset]:
                        break
                    offset += 1
                except IndexError:
                    return i + 1

    return 0


def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    patterns = itertools.groupby(lines, lambda line: line != "")
    patterns = (list(pattern) for (key, pattern) in patterns)
    patterns = filter(lambda p: p != [""], patterns)

    answer = 0
    for i, pattern in enumerate(patterns):
        h = reflection(pattern)
        pattern = [
            "".join([pattern[i][j] for i in range(len(pattern))])
            for j in range(len(pattern[0]))
        ]
        v = reflection(pattern)

        print(f"{i=}, {h=}, {v=}")
        assert (h == 0) ^ (v == 0)
        answer += v + h * 100

    print(answer)


if __name__ == '__main__':
    main()
