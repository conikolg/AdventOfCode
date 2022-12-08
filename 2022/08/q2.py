import numpy as np


def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    lines = [list(map(int, list(line))) for line in lines]
    lines = np.array(lines)

    n, m = lines.shape
    big = 0
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            up = 1
            while i - up >= 0 and lines[i - up, j] < lines[i, j]: up += 1
            if i - up == -1:
                up -= 1

            down = 1
            while i + down < n and lines[i + down, j] < lines[i, j]: down += 1
            if i + down == n:
                down -= 1

            left = 1
            while j - left >= 0 and lines[i, j - left] < lines[i, j]: left += 1
            if j - left == -1:
                left -= 1

            right = 1
            while j + right < m and lines[i, j + right] < lines[i, j]: right += 1
            if j + right == m:
                right -= 1

            big = max(big, up * down * left * right)

    print(big)


if __name__ == '__main__':
    main()
