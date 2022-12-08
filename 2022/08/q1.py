import numpy as np


def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    lines = [list(map(int, list(line))) for line in lines]
    lines = np.array(lines)
    count = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if i == 0 or i == len(lines) - 1 or j == 0 or j == len(lines[i]) - 1:
                count += 1
                continue
            else:
                h = lines[i, j]
                if h > max(lines[i, :j]) or h > max(lines[i, j + 1:]) or h > max(lines[:i, j]) or h > max(
                        lines[i + 1:, j]):
                    count += 1
                    continue

    print(count)


if __name__ == '__main__':
    main()
