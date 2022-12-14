def load_file(filename):
    with open(filename, "r") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


def main(lines):
    paths = []
    for line in lines:
        points = line.split(" -> ")
        path = []
        for point in points:
            path.append(tuple(map(int, point.split(","))))
        paths.append(path)

    grid = dict()
    for path in paths:
        for i in range(len(path) - 1):
            if path[i][0] != path[i + 1][0]:  # horizontal
                for x in range(path[i][0], path[i + 1][0] + 1):
                    grid[(x, path[i][1])] = 'r'
                for x in range(path[i][0], path[i + 1][0] - 1, -1):
                    grid[(x, path[i][1])] = 'r'
            else:  # vertical
                for y in range(path[i][1], path[i + 1][1] + 1):
                    grid[(path[i][0], y)] = 'r'
                for y in range(path[i][1], path[i + 1][1] - 1, -1):
                    grid[(path[i][0], y)] = 'r'

    print(grid.keys())
    count = 0
    # make new sand
    while True:
        sand = [500, 0]
        # move as needed
        while True:
            # move down if possible
            if (sand[0], sand[1] + 1) not in grid:
                sand[1] += 1
                # print("sand down to", sand)
                if sand[1] >= 1000:
                    print("sand fell out at", sand)
                    print(count)
                    return
            # move to right spot
            elif (sand[0] - 1, sand[1] + 1) not in grid:
                sand = [sand[0] - 1, sand[1] + 1]
                print("sand pushed to", sand)
                continue
            elif (sand[0] + 1, sand[1] + 1) not in grid:
                sand = [sand[0] + 1, sand[1] + 1]
                print("sand pushed to", sand)
                continue
            else:
                print("placed sand at", sand, "\n")
                grid[tuple(sand)] = 's'
                count += 1
                break


if __name__ == '__main__':
    main(load_file(filename="in"))
