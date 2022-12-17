def load_file(filename):
    with open(filename, "r") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


def is_rock_colliding(shape: list[list], pos: list[int], heights: list[set[int]]):
    h, w = len(shape), len(shape[0])

    # Bounding box check - left
    if pos[0] < 0:
        return True
    # Bounding box check - right
    if pos[0] + w - 1 > 6:
        return True

    # Individual point check
    for y in range(h):
        for x in range(w):
            if shape[y][x]:
                if pos[1] - y in heights[x + pos[0]] or pos[1] - y == 0:
                    return True

    return False


def main(lines):
    line = lines[0]
    line_idx = 0

    heights = [set() for _ in range(7)]

    rock_shapes = [
        [
            [True, True, True, True]
        ],
        [
            [False, True, False],
            [True, True, True],
            [False, True, False]
        ],
        [
            [False, False, True],
            [False, False, True],
            [True, True, True]
        ],
        [
            [True],
            [True],
            [True],
            [True]
        ],
        [
            [True, True],
            [True, True]
        ]
    ]
    shape_idx = 0
    rocks = 0

    while rocks < 2022:
        # Spawn rock
        rock_shape = rock_shapes[shape_idx]
        # print(shape_idx, end=" ")
        shape_idx = (shape_idx + 1) % len(rock_shapes)
        start_h = 0
        for h_set in heights:
            if len(h_set) != 0:
                start_h = max(start_h, max(h_set))
        rock_pos = [2, start_h + 3 + len(rock_shape)]

        while True:
            # Rock push
            # print("pre push", rock_pos)
            rock_pos[0] += 1 if line[line_idx] == ">" else -1
            if is_rock_colliding(rock_shape, rock_pos, heights):
                rock_pos[0] -= 1 if line[line_idx] == ">" else -1
            line_idx = (line_idx + 1) % len(line)
            # print("postpush", rock_pos)

            # Rock fall
            rock_pos[1] -= 1
            if is_rock_colliding(rock_shape, rock_pos, heights):
                rock_pos[1] += 1

                # Put rock in place
                # print("collide at ", rock_pos)
                for y in range(len(rock_shape)):
                    for x in range(len(rock_shape[y])):
                        if rock_shape[y][x]:
                            heights[rock_pos[0] + x].add(rock_pos[1] - y)
                break
            # print("postfall", rock_pos)

        rocks += 1

    start_h = 0
    for h_set in heights:
        if len(h_set) != 0:
            start_h = max(start_h, max(h_set))
    print(start_h)


if __name__ == '__main__':
    main(load_file(filename="in"))
