import re


def load_file(filename):
    with open(filename, "r") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


def main(lines):
    monkeys = []
    while len(lines) > 0:
        num = int(re.search(r"^Monkey (\d+):", lines.pop(0)).groups()[0])
        items: str = lines.pop(0).split(":")[1]
        items: list = list(map(int, map(str.strip, items.split(","))))
        op: str = lines.pop(0).split("=")[1].strip()
        test: int = int(lines.pop(0).split(" ")[-1])
        toss: list = [int(lines.pop(0).split(" ")[-1]), int(lines.pop(0).split(" ")[-1])]
        monkeys.append({"num": num, "items": items, "op": op, "test": test, "toss": toss, "inspect": 0})
        lines.pop(0)

    lcm = 1
    for monkey in monkeys:
        lcm *= monkey["test"]
    print(f"{lcm=}")

    for r in range(10000):
        if r % 1000 == 0:
            print(f"{r=}")
        for monkey in monkeys:
            while len(monkey["items"]) > 0:
                old = monkey["items"].pop(0)
                new_worry = eval(monkey["op"])
                new_worry = new_worry % lcm
                if new_worry % monkey["test"] == 0:
                    monkeys[monkey["toss"][0]]["items"].append(new_worry)
                else:
                    monkeys[monkey["toss"][1]]["items"].append(new_worry)
                monkey["inspect"] += 1

    monkeys.sort(key=lambda m: m["inspect"])
    print(monkeys[-1]["inspect"], monkeys[-2]["inspect"])
    print(monkeys[-1]["inspect"] * monkeys[-2]["inspect"])


if __name__ == '__main__':
    main(load_file(filename="in"))
