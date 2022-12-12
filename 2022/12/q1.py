import operator


def load_file(filename):
    with open(filename, "r") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


def main(lines):
    grid: list[list[int]] = [list(line) for line in lines]

    start, end = None, None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start = (i, j)
                grid[i][j] = 'a'
            elif grid[i][j] == 'E':
                end = (i, j)
                grid[i][j] = 'z'

            grid[i][j] = ord(grid[i][j]) - ord('a')

    print(start, end)
    for line in grid:
        print(line)

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = [(start, 0)]
    visited = set()
    while q:
        loc, dist = q.pop(0)
        i, j = loc
        if loc in visited:
            continue

        if loc == end:
            print(loc, dist)
            return
        visited.add(loc)

        for offset in moves:
            ii, jj = tuple(map(operator.add, loc, offset))
            if not (0 <= ii < len(grid)):
                continue
            if not (0 <= jj < len(grid[0])):
                continue

            if grid[ii][jj] <= grid[i][j] + 1:
                q.append(((ii, jj), dist + 1))


if __name__ == '__main__':
    main(load_file(filename="in"))
