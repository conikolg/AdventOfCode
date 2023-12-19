def main():
    with open("in.txt", "r") as infile:
        lines = [list(line.strip()) for line in infile.readlines()]

    for j in range(len(lines[0])):
        column = "".join(lines[i][j] for i in range(len(lines)))
        parts: [str] = column.split("#")
        for i, p in enumerate(parts):
            parts[i] = "".join(sorted(p, reverse=True))
        column = "#".join(parts)
        for i in range(len(lines)):
            lines[i][j] = column[i]

    answer = 0
    for i in range(len(lines)):
        points = len(lines) - i
        answer += points * lines[i].count("O")

    print(answer)


if __name__ == '__main__':
    main()
