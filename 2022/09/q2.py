def touching(h, t):
    return abs(h[0] - t[0]) < 2 and abs(h[1] - t[1]) < 2


def follow(head, tail):
    if touching(head, tail):
        return
        # Same column
    elif head[0] == tail[0]:
        if head[1] > tail[1]:
            tail[1] += 1
        else:
            tail[1] -= 1
    # Same row
    elif head[1] == tail[1]:
        if head[0] < tail[0]:
            tail[0] -= 1
        else:
            tail[0] += 1
    # Diagonal
    else:
        if head[0] > tail[0]:
            tail[0] += 1
        else:
            tail[0] -= 1
        if head[1] > tail[1]:
            tail[1] += 1
        else:
            tail[1] -= 1


def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    knots = list()
    for i in range(10):
        knots.append([0, 0])
    visited = set()
    visited.add(tuple(knots[-1]))

    for line in lines:
        direction, distance = tuple(line.split())
        distance = int(distance)
        for i in range(distance):
            if direction == "U":
                knots[0][1] += 1
            elif direction == "D":
                knots[0][1] -= 1
            elif direction == "L":
                knots[0][0] -= 1
            elif direction == "R":
                knots[0][0] += 1

            for j in range(0, len(knots) - 1):
                follow(knots[j], knots[j + 1])

            visited.add(tuple(knots[-1]))

    print(len(visited))


if __name__ == '__main__':
    main()
