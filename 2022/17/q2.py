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

    states = set()

    while rocks < 1e12:
        if rocks % 100 == 0:
            print(f"debug line: {rocks=}")

        # Spawn rock
        rock_shape = rock_shapes[shape_idx]
        # print(shape_idx, end=" ")
        shape_idx = (shape_idx + 1) % len(rock_shapes)

        """ Step 1: Check for a cycle. Let the program run for a few seconds.
        #           There is a consistent difference in rock count for a given state. Ctrl F for the first state.
        #           Note the rock of the first state, and the rock difference and height difference between the 1st
        #           occurrence of the state and the second occurrence of the same state
        max_heights = tuple(max(he, default=0) for he in heights)
        rel_heights = tuple(map(lambda h: h - max(max_heights), max_heights))
        state = (rel_heights, shape_idx, line_idx)
        if state in states:
            print(f"found repeated top state: {rocks=} {state=} {max(max_heights)=}")
        else:
            states.add(state)
        # """

        # """ Step 2: Use step 1 output to skip forward until 1e12 rocks
        first_finished_cycle_rock = 1863  # 1st rock count from part 1
        rock_skip = 1695  # difference in rock counts from part 1
        height_skip = 2610  # difference in max heights from part 1
        if rocks == first_finished_cycle_rock:
            print(f"skipped from {rocks=} to ", end="")
            skip_count = int(1e12 - first_finished_cycle_rock) // rock_skip
            rocks += rock_skip * skip_count
            for i in range(len(heights)):
                tmp = list(map(lambda h: h + height_skip * skip_count, heights[i]))
                heights[i] = set(tmp)
            print(f"{rocks=}")
        # """

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
