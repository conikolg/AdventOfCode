import re


def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    numbers = "zero one two three four five six seven eight nine".split()

    answer = 0
    for line in lines:
        matches = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)

        number = ""
        try:
            number += str(int(matches[0]))
        except Exception:
            number += str(numbers.index(matches[0]))

        try:
            number += str(int(matches[-1]))
        except Exception:
            number += str(numbers.index(matches[-1]))

        print(matches, number)
        answer += int(number)

    print(answer)


if __name__ == '__main__':
    main()
