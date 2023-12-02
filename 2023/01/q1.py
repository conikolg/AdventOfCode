import re


def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    answer = 0
    for line in lines:
        matches = re.findall(r"\d", line)
        if len(matches) == 1:
            matches *= 2
        elif len(matches) > 2:
            matches = [matches[0], matches[-1]]

        # print(matches)
        answer += int(''.join(matches))

    print(answer)


if __name__ == '__main__':
    main()
