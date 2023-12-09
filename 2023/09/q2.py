import utils


def predict(n: [int]):
    diff = []
    for i in range(len(n) - 1, 0, -1):
        diff.insert(0, n[i] - n[i-1])

    if all(d == 0 for d in diff):
        return n[0]

    next_diff = predict(diff)
    return n[0] - next_diff


def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    answer = 0
    for line in lines:
        numbers: [int] = utils.int_split(line)
        nxt = predict(numbers)
        answer += nxt
        print(nxt)

    print(answer)


if __name__ == '__main__':
    main()
