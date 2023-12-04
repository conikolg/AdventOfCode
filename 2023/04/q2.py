def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    answer = 0
    copies = []
    for line in lines:
        if len(copies) == 0:
            copies.append(0)

        game = line.split(":")
        card_num = int(game[0].split()[1])
        win, have = game[1].split("|")
        win = list(map(int, win.split()))
        have = list(map(int, have.split()))

        card_count = copies.pop(0)
        answer += card_count + 1
        matches = set(win).intersection(set(have))
        if len(matches) > 0:
            for i in range(len(matches)):
                if i < len(copies):
                    copies[i] += card_count + 1
                else:
                    copies.append(card_count + 1)

        # print(f"after game {card_num} copies = {copies}")

    print(answer)


if __name__ == '__main__':
    main()
