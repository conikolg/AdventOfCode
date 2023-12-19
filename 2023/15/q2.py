import pprint
import re


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

    boxes = {
        i: list()
        for i in range(256)
    }

    steps = lines[0].split(",")
    for step in steps:
        label, op, focus = re.findall(r"(\w+)([=-])(\d?)", step)[0]
        box = HASH(label)
        if op == "-":
            for i in reversed(range(len(boxes[box]))):
                if boxes[box][i][0] == label:
                    boxes[box].pop(i)
                    break
        else:
            for i in range(len(boxes[box])):
                if boxes[box][i][0] == label:
                    boxes[box][i][1] = focus
                    break
            else:
                boxes[box].append([label, focus])

    pprint.pprint({
        box: boxes[box]
        for box in boxes
        if len(boxes[box]) > 0
    })

    power = 0
    for box in boxes:
        if len(boxes[box]) > 0:
            temp = box + 1
            for i, (_, focus) in enumerate(boxes[box]):
                power += (box + 1) * (i + 1) * int(focus)

    print(power)


if __name__ == '__main__':
    main()
