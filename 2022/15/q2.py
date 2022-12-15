import re


def load_file(filename):
    with open(filename, "r") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


def mhd(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def merge(intervals):
    idx, i = 0, 1
    while i < len(intervals):
        if intervals[idx][0] <= intervals[i][0] <= intervals[idx][1]:
            intervals[idx][1] = max(intervals[idx][1], intervals[i][1])
            intervals.pop(i)
        else:
            idx += 1
            i += 1


def main(lines):
    sb = dict()
    for line in lines:
        x, y, x2, y2 = (
            re.search(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line).groups())
        x, y, x2, y2 = tuple(map(int, (x, y, x2, y2)))
        sb[(x, y)] = (x2, y2), mhd((x, y), (x2, y2))

    for row in range(0, int(4e6)):
        covered = []
        for sensor, (b, d) in sb.items():
            y_diff = abs(sensor[1] - row)
            if y_diff > d:
                continue
            xr = (sensor[0] - (d - y_diff), sensor[0] + (d - y_diff))
            covered.append(list(xr))

        covered.sort()
        merge(covered)
        if row % 100_000 == 0:
            print(f"{row=}")
        if len(covered) != 1:
            print(covered)
            print(int(4e6) * (covered[0][1] + 1) + row)


if __name__ == '__main__':
    main(load_file(filename="in"))
