strength = "AKQT98765432J"  # J is now the weakest


def card_strength_tuple(cards: str):
    return tuple(
        20 - strength.index(c)
        for c in cards
    )


def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    hands: list = [
        line.split()
        for line in lines
    ]

    for hand in hands:
        counts = {e: hand[0].count(e) for e in set(hand[0])}
        # Shift all the counts of J into most common of other cards
        if 'J' in counts:
            jokers = counts['J']
            del counts['J']
            if jokers == 5:
                counts['J'] = 5
            else:
                add_to = max(counts.keys(), key=lambda k: counts[k])
                counts[add_to] += jokers

        if 5 in counts.values():
            hand.append(5)
        elif 4 in counts.values():
            hand.append(4)
        elif 3 in counts.values():
            if 2 in counts.values():
                hand.append(3.5)
            else:
                hand.append(3)
        elif 2 in counts.values():
            if sorted(list(counts.values())) == [1, 2, 2]:
                hand.append(2.5)
            else:
                hand.append(2)
        else:
            hand.append(1)

        hand[1] = int(hand[1])
        hand.append(card_strength_tuple(hand[0]))

    hands.sort(key=lambda h: (h[2], h[3]))

    answer = 0
    for i, h in enumerate(hands):
        print(h, '\t', i + 1, h[1], (i + 1) * h[1])
        answer += (i + 1) * h[1]
    print(answer)


if __name__ == '__main__':
    main()
