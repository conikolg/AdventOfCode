import operator


def get_grid_neighbors(grid: [list | str], pos: tuple[int, int],
                       cardinal_directions: bool = True, ordinal_directions: bool = False,
                       valid_only: bool = True, get_positions: bool = True, get_values: bool = False):
    if not get_values and not get_positions:
        raise Exception("Must request something to yield")
    if not cardinal_directions and not ordinal_directions:
        raise Exception("Must request some direction to move")

    directions = []
    if cardinal_directions:
        directions += [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
    if ordinal_directions:
        directions += [(-1, 1), (1, 1), (1, -1), (-1, -1)]  # northwest, southwest, southeast, northeast

    for direction in directions:
        i, j = add_tuples(pos, direction)

        # Valid position
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]):
            if get_positions and not get_values:
                yield i, j
            elif not get_positions and get_values:
                yield grid[i][j]
            else:
                yield (i, j), grid[i][j]
        # Invalid position
        elif not valid_only:
            if get_positions and not get_values:
                yield i, j
            elif not get_positions and get_values:
                yield None
            else:
                yield (i, j), None


def line_groups(lines: list[str], delimiter: str = ""):
    idx, groups = 0, [[]]
    for line in lines:
        if line != delimiter:
            groups[idx].append(line)
        else:
            groups.append([])
            idx += 1

    groups = list(filter(lambda g: len(g) != 0, groups))
    for grp in groups:
        yield grp


def as_grid(data, fn=(lambda x: x)):
    return [list(map(fn, d)) for d in data]


def add_tuples(a, b):
    return tuple(map(operator.add, a, b))


def int_split(s: str) -> [int]:
    return list(map(int, s.split()))


def print_return(func):
    def f(*args, **kwargs):
        ret = func(*args, **kwargs)
        print(ret)
        return ret

    return f


def transpose(matrix: [list]) -> [list]:
    return [
        [matrix[j][i] for j in range(len(matrix))]
        for i in range(len(matrix[0]))
    ]


def rotate_cw(matrix: [list]) -> [list]:
    return [
        list(reversed([matrix[i][j] for i in range(len(matrix))]))
        for j in range(len(matrix[0]))
    ]
