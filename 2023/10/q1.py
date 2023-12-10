def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    si, sj = [(i, j) for i in range(len(lines)) for j in range(len(lines[i])) if lines[i][j] == "S"][0]
    prv, cur, dist = (si, sj), None, 1
    if lines[si - 1][sj] in "7F|":
        cur = (si - 1, sj)
    elif lines[si + 1][sj] in "LJ|":
        cur = (si + 1, sj)
    elif lines[si][sj - 1] in "FL-":
        cur = (si, sj - 1)
    elif lines[si][sj + 1] in "7J-":
        cur = (si, sj + 1)

    while cur != (si, sj):
        print(lines[cur[0]][cur[1]])
        opts = []
        u, d, l, r = [-1, 0], [1, 0], [0, -1], [0, 1]

        if lines[cur[0]][cur[1]] == "|":
            opts += [u, d]
        elif lines[cur[0]][cur[1]] == "-":
            opts += [l, r]
        elif lines[cur[0]][cur[1]] == "L":
            opts += [u, r]
        elif lines[cur[0]][cur[1]] == "J":
            opts += [u, l]
        elif lines[cur[0]][cur[1]] == "7":
            opts += [d, l]
        elif lines[cur[0]][cur[1]] == "F":
            opts += [d, r]

        opts = [
            (cur[0] + direction[0], cur[1] + direction[1])
            for direction in opts
        ]
        # print(opts, prv)
        if opts[0] == prv:
            prv = cur
            cur = opts[1]
        else:
            prv = cur
            cur = opts[0]
        dist += 1

    print(dist // 2)


if __name__ == '__main__':
    main()
