import utils

cache = set()
energized = set()


def simulate(lines: [str], dr: tuple[int, int], pos: tuple[int, int]) -> None:
    q = [(dr, pos)]

    while len(q) > 0:
        dr, pos = q.pop(0)
        i, j = pos

        # off grid
        if i < 0 or i >= len(lines) or j < 0 or j >= len(lines[i]):
            continue
        # already seen this combo
        if (dr, pos) in cache:
            continue

        cache.add((dr, pos))
        energized.add(pos)

        # pass through
        if lines[i][j] == "." or (dr[0] == 0 and lines[i][j] == "-") or (dr[1] == 0 and lines[i][j] == "|"):
            q.append((dr, utils.add_tuples(dr, pos)))
        # moving horizontally, split vertically
        elif dr[0] == 0 and lines[i][j] == "|":
            q.append(((1, 0), utils.add_tuples((1, 0), pos)))
            q.append(((-1, 0), utils.add_tuples((-1, 0), pos)))
        # moving vertically, split horizontally
        elif dr[1] == 0 and lines[i][j] == "-":
            q.append(((0, 1), utils.add_tuples((0, 1), pos)))
            q.append(((0, -1), utils.add_tuples((0, -1), pos)))
        # hit mirror
        elif lines[i][j] == "/":
            if dr == (1, 0):
                q.append(((0, -1), utils.add_tuples((0, -1), pos)))
            elif dr == (-1, 0):
                q.append(((0, 1), utils.add_tuples((0, 1), pos)))
            elif dr == (0, 1):
                q.append(((-1, 0), utils.add_tuples((-1, 0), pos)))
            elif dr == (0, -1):
                q.append(((1, 0), utils.add_tuples((1, 0), pos)))
        elif lines[i][j] == "\\":
            if dr == (1, 0):
                q.append(((0, 1), utils.add_tuples((0, 1), pos)))
            elif dr == (-1, 0):
                q.append(((0, -1), utils.add_tuples((0, -1), pos)))
            elif dr == (0, 1):
                q.append(((1, 0), utils.add_tuples((1, 0), pos)))
            elif dr == (0, -1):
                q.append(((-1, 0), utils.add_tuples((-1, 0), pos)))


def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    simulate(lines, (0, 1), (0, 0))
    print(len(energized))


if __name__ == '__main__':
    main()
