import pprint
import re
from collections import defaultdict


def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    games = defaultdict(lambda: defaultdict(lambda: 0))
    for line in lines:
        game, hands = line.split(":")
        game_id = int(re.findall(r"\d+", game)[0])
        hands = hands.split(";")
        for hand in hands:
            groups = hand.split(",")
            for grp in groups:
                count = int(re.findall(r"\d+", grp)[0])
                color = re.findall(r"red|blue|green", grp)[0]
                games[game_id][color] = max(games[game_id][color], count)

    pprint.pprint(games)

    answer = 0
    for game_id, game in games.items():
        answer += game["red"] * game["blue"] * game["green"]

    print(answer)


if __name__ == '__main__':
    main()
