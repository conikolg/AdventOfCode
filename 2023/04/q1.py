def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    answer = 0
    for line in lines:
        win, have = line.split(":")[1].split("|")
        win = list(map(int, win.split()))
        have = list(map(int, have.split()))

        matches = set(win).intersection(set(have))
        if len(matches) > 0:
            answer += 2 ** (len(matches) - 1)

    print(answer)


if __name__ == '__main__':
    main()
