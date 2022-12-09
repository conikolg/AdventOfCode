def touching(h, t):
    return abs(h[0] - t[0]) < 2 and abs(h[1] - t[1]) < 2


def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    head = [0, 0]
    tail = [0, 0]
    visited = set()
    visited.add(tuple(tail))

    for line in lines:
        direction, distance = tuple(line.split())
        distance = int(distance)
        for i in range(distance):
            if direction == "U":
                head[1] += 1
            elif direction == "D":
                head[1] -= 1
            elif direction == "L":
                head[0] -= 1
            elif direction == "R":
                head[0] += 1

            if touching(head, tail):
                continue
            # Same column
            elif head[0] == tail[0]:
                if direction == "U":
                    tail[1] += 1
                else:
                    tail[1] -= 1
            # Same row
            elif head[1] == tail[1]:
                if direction == "L":
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

            visited.add(tuple(tail))

    print(len(visited))


if __name__ == '__main__':
    main()
