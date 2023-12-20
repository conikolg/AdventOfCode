import copy

import utils


def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    seed_ranges: [int] = utils.int_split(lines.pop(0).split(":")[1])
    seed_ranges: [[int]] = sorted([
        [seed_ranges[i], seed_ranges[i] + seed_ranges[i + 1]]
        for i in range(0, len(seed_ranges), 2)
    ])
    # print(f"initial {seed_ranges=}")

    conversions = []
    maps: [[str]] = list(utils.line_groups(lines))
    for Map in maps:
        Map.pop(0)
        information = [utils.int_split(m) for m in Map]
        conversions.append([
            [info[1] for info in information],  # src
            [info[0] for info in information],  # dst
            [info[2] for info in information]  # length of range
        ])

    # Go through all maps
    for map_idx, conversion in enumerate(conversions):
        # print(f"\ngoing through map {map_idx}")
        seed_ranges_to_try = sorted(copy.deepcopy(seed_ranges))
        # Split ranges anytime an endpoint of a map range is inside a seed range
        for i in range(len(conversion[0])):
            first_seed = conversion[0][i]
            for j, seed_range in enumerate(seed_ranges_to_try):
                if seed_range[0] <= first_seed < seed_range[1]:
                    seed_ranges_to_try.append([seed_range[0], first_seed + 1])
                    seed_ranges_to_try.append([first_seed, seed_range[1]])
                    seed_ranges_to_try.pop(j)
                    break

            last_seed = conversion[0][i] + conversion[2][i] - 1
            for j, seed_range in enumerate(seed_ranges_to_try):
                if seed_range[0] <= last_seed < seed_range[1]:
                    seed_ranges_to_try.append([seed_range[0], last_seed + 1])
                    seed_ranges_to_try.append([last_seed, seed_range[1]])
                    seed_ranges_to_try.pop(j)
                    break

        # These are the seeds to pass into the map
        seed_ranges_to_try = sorted(seed_ranges_to_try)
        # print(f"before map: {seed_ranges=}, {conversion=}, {seed_ranges_to_try=}")

        # Convert only the start seed for a range - use length of range to get new end seed
        for i in range(len(seed_ranges_to_try)):
            range_length = seed_ranges_to_try[i][1] - seed_ranges_to_try[i][0]
            first_seed = convert(seed_ranges_to_try[i][0], *conversion)
            seed_ranges_to_try[i] = [first_seed, first_seed + range_length]

        # These are the new ranges for the next map
        seed_ranges_to_try = sorted(seed_ranges_to_try)
        # print(f" after map: {seed_ranges=}, {conversion=}, {seed_ranges_to_try=}")
        seed_ranges = seed_ranges_to_try

    print(seed_ranges[0][0])


def convert(seed: int, src: [int], dst: [int], length: [int]):
    for i in range(len(src)):
        if src[i] <= seed < src[i] + length[i]:
            return dst[i] + (seed - src[i])
    return seed


if __name__ == '__main__':
    main()
