import re
from collections import defaultdict


def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    sizes = defaultdict(lambda: 0)
    path = list()

    for line in lines:
        if line.startswith("$"):
            args = line.split(" ")[1:]
            if args[0] == "cd":
                if args[1] == "..":
                    folder_size = sizes["/".join(path)]
                    path.pop(-1)
                    sizes["/".join(path)] += folder_size
                else:
                    path.append(args[1])
        elif re.match(r"\d+ .*", line):
            size, filename = line.split(" ")
            size = int(size)
            sizes["/".join(path)] += size

    total = 0
    for k, v in sizes.items():
        if v <= 100000:
            total += v
    print(total)


if __name__ == '__main__':
    main()
