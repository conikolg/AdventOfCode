import utils


def simulate(lines: [str], dr: tuple[int, int], pos: tuple[int, int]) -> int:
    cache = set()
    energized = set()
    q = [(dr, pos)]

    while len(q) > 0:
        curr_dir, curr_pos = q.pop(0)
        i, j = curr_pos

        # off grid
        if i < 0 or i >= len(lines) or j < 0 or j >= len(lines[i]):
            continue
        # already seen this combo
        if (curr_dir, curr_pos) in cache:
            continue

        cache.add((curr_dir, curr_pos))
        energized.add(curr_pos)

        # pass through
        if lines[i][j] == "." or (curr_dir[0] == 0 and lines[i][j] == "-") or (curr_dir[1] == 0 and lines[i][j] == "|"):
            q.append((curr_dir, utils.add_tuples(curr_dir, curr_pos)))
        # moving horizontally, split vertically
        elif curr_dir[0] == 0 and lines[i][j] == "|":
            q.append(((1, 0), utils.add_tuples((1, 0), curr_pos)))
            q.append(((-1, 0), utils.add_tuples((-1, 0), curr_pos)))
        # moving vertically, split horizontally
        elif curr_dir[1] == 0 and lines[i][j] == "-":
            q.append(((0, 1), utils.add_tuples((0, 1), curr_pos)))
            q.append(((0, -1), utils.add_tuples((0, -1), curr_pos)))
        # hit mirror
        elif lines[i][j] == "/":
            if curr_dir == (1, 0):
                q.append(((0, -1), utils.add_tuples((0, -1), curr_pos)))
            elif curr_dir == (-1, 0):
                q.append(((0, 1), utils.add_tuples((0, 1), curr_pos)))
            elif curr_dir == (0, 1):
                q.append(((-1, 0), utils.add_tuples((-1, 0), curr_pos)))
            elif curr_dir == (0, -1):
                q.append(((1, 0), utils.add_tuples((1, 0), curr_pos)))
        elif lines[i][j] == "\\":
            if curr_dir == (1, 0):
                q.append(((0, 1), utils.add_tuples((0, 1), curr_pos)))
            elif curr_dir == (-1, 0):
                q.append(((0, -1), utils.add_tuples((0, -1), curr_pos)))
            elif curr_dir == (0, 1):
                q.append(((1, 0), utils.add_tuples((1, 0), curr_pos)))
            elif curr_dir == (0, -1):
                q.append(((-1, 0), utils.add_tuples((-1, 0), curr_pos)))

    print(f"Completed sim for {dr=}, {pos=}, {len(energized)=}")
    return len(energized)


def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    options = []
    options += [((0, 1), (i, 0)) for i in range(len(lines))]
    options += [((0, -1), (i, len(lines[i]) - 1)) for i in range(len(lines))]
    options += [((1, 0), (0, j)) for j in range(len(lines[0]))]
    options += [((-1, 0), (len(lines) - 1, j)) for j in range(len(lines[0]))]

    print(max([simulate(lines, *opt) for opt in options]))


if __name__ == '__main__':
    main()
