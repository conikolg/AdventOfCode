def HASH(s: str) -> int:
    value = 0
    for c in s:
        value += ord(c)
        value *= 17
        value %= 256
    return value


def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    steps = lines[0].split(",")
    answer = 0
    for step in steps:
        answer += HASH(step)
    print(answer)


if __name__ == '__main__':
    main()
