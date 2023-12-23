import heapq

import utils


def heuristic(next_pos, grid):
    return abs(len(grid) - 1 - next_pos[0]) + abs(len(grid[0]) - 1 - next_pos[1])


def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    grid: [[int]] = [
        list(map(int, list(line)))
        for line in lines
    ]

    visited: dict = dict()
    pq = [(0, 0, ("h", (0, 0)))]
    heapq.heappush(pq, (0, 0, ("v", (0, 0))))

    while len(pq) > 0:
        candidate = heapq.heappop(pq)
        predicted_heat_loss, heat_loss, move = candidate
        if move in visited:
            continue

        jump_dir, pos = move
        visited[move] = heat_loss

        # Done?
        if pos == (len(grid) - 1, len(grid[0]) - 1):
            print(heat_loss, move)
            return

        # Define allowed directions
        if jump_dir == "h":
            dirs = [(1, 0), (-1, 0), (2, 0), (-2, 0), (3, 0), (-3, 0)]
        else:
            dirs = [(0, 1), (0, -1), (0, 2), (0, -2), (0, 3), (0, -3)]

        # Generate next options
        for next_dir in dirs:
            next_pos = utils.add_tuples(pos, next_dir)
            if not (0 <= next_pos[0] < len(grid)) or not (0 <= next_pos[1] < len(grid[0])):
                continue
            loss = 0
            if next_dir[0] == 0:
                for j in (range(1, next_dir[1] + 1) if next_dir[1] > 0 else range(-1, next_dir[1] - 1, -1)):
                    loss += grid[pos[0]][pos[1] + j]
            else:
                for i in (range(1, next_dir[0] + 1) if next_dir[0] > 0 else range(-1, next_dir[0] - 1, -1)):
                    loss += grid[pos[0] + i][pos[1]]
            next_heat_loss = heat_loss + loss
            heapq.heappush(pq, (
                next_heat_loss + heuristic(next_pos, grid),
                next_heat_loss,
                (("h" if next_dir[1] != 0 else "v"), next_pos)
            ))


if __name__ == '__main__':
    main()
