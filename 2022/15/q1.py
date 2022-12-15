import re


def load_file(filename):
    with open(filename, "r") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


def mhd(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def main(lines):
    sb = dict()
    for line in lines:
        x, y, x2, y2 = (
            re.search(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line).groups())
        x, y, x2, y2 = tuple(map(int, (x, y, x2, y2)))
        sb[(x, y)] = (x2, y2), mhd((x, y), (x2, y2))

    row = int(2e6)
    count = 0
    covered = []

    for sensor, (b, d) in sb.items():
        y_diff = abs(sensor[1] - row)
        if y_diff > d:
            continue
        xr = (sensor[0] - (d - y_diff), sensor[0] + (d - y_diff))
        covered.append(xr)

    print(covered)
    beacons = [b for b, _ in sb.values()]
    for x in range(min(c[0] for c in covered), max(c[1] for c in covered) + 1):
        if ((x, row) not in beacons) and any([xr[0] <= x <= xr[1] for xr in covered]):
            count += 1

    print(count)


if __name__ == '__main__':
    main(load_file(filename="in"))
