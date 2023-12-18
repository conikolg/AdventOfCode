import functools
import re


def possible(group: str, leading: int, length: int):
    """ Returns length of string matched """

    # These must be this many leading dots
    if leading > 0 and not group.startswith("?" * leading):
        return 0
    # These must then be this many broken pipes
    if re.fullmatch(r"[#?]+", group[leading:leading + length]) is None:
        return 0
    # Must be a delimiter - EOF or room for a dot
    if leading + length == len(group):
        return len(group)
    if group[leading + length] == "?":
        return leading + length + 1

    return 0


@functools.lru_cache
def fit(groups: [str], known: [int]):
    # print(f"fit {groups=}, {known=}")
    if len(known) == 0:
        # Success if all remaining groups are ?
        if len(groups) == 0 or all(re.fullmatch(r"\?+", grp) is not None for grp in groups):
            return 1
        # No match
        return 0

    # There should be another group that needs a match
    if len(groups) == 0:
        return 0

    # Try to make matches
    matches = 0
    for i in range(len(groups[0]) - known[0] + 1):
        consumed: int = possible(groups[0], i, known[0])
        if consumed == 0:
            pass
        elif consumed == len(groups[0]):
            matches += fit(groups[1:], known[1:])
        else:
            modified_group = groups[0][consumed:]
            matches += fit((modified_group,) + groups[1:], known[1:])

    # What happens if this group contains no broken pipes?
    if all(c == "?" for c in groups[0]):
        matches += fit(groups[1:], known)

    return matches


def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    answer = 0
    for line in lines:
        springs, known = line.split(" ")
        known: [int] = list(map(int, known.split(",")))

        springs = "?".join([springs] * 5)
        known *= 5

        groups = re.findall(r"[#?]+", springs)
        r = fit(tuple(groups), tuple(known))
        print(groups, known, r)
        answer += r

    print(answer)


if __name__ == '__main__':
    main()
