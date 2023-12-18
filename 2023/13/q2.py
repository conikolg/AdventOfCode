import itertools


def spread(p: [str], i: int, smudge: bool, offset: int = 0):
    while True:
        # Smudge must be used if reflection is complete
        if i - offset < 0:
            return not smudge
        if i + 1 + offset == len(p):
            return not smudge

        # Keep going if same
        if p[i - offset] == p[i + 1 + offset]:
            pass
        # If smudge is available and diff is 1 character, use smudge
        elif smudge and sum(
                1 if p[i - offset][j] != p[i + 1 + offset][j] else 0 for j in range(len(p[i - offset]))) == 1:
            smudge = False
        # If smudge already used or diff isn't one character, fail
        else:
            return False

        offset += 1


def reflection(p: [str]):
    for i in range(len(p) - 1):
        # These two rows perfectly match
        if p[i] == p[i + 1]:
            # See if one fix elsewhere is good
            if spread(p, i, True):
                return i + 1
        # Else, maybe a fix here will cause a reflection
        elif sum(1 if p[i][j] != p[i + 1][j] else 0 for j in range(len(p[i]))) == 1:
            if spread(p, i, False, offset=1):
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
