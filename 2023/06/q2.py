def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    time: int = int("".join(lines.pop(0).split(":")[1].split()))
    distance: int = int("".join(lines.pop(0).split(":")[1].split()))

    min_press = None
    max_press = None

    for t in range(1, time):
        dist = (time - t) * t
        if dist > distance:
            min_press = t
            break

    for t in range(time, 0, -1):
        dist = (time - t) * t
        if dist > distance:
            max_press = t
            break

    print(max_press - min_press + 1)


if __name__ == '__main__':
    main()
