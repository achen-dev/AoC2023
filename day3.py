INPUT_FILE = "inputs/day3"


def find_neighbors(col, row, board):
    neighbors_coords_list = []
    neighbors_list = []
    neighbor_directions = [(0, 1), (1, 1), (1, 0), (0, -1), (-1, -1), (-1, 0), (1, -1), (-1, 1)]
    for direction in neighbor_directions:
        if (0 <= col + direction[1] < len(board)
                and 0 <= row + direction[0] < len(board[0])):
            neighbors_coords_list.append((col + direction[1], row + direction[0]))
            neighbors_list.append(board[row+direction[0]][col+direction[1]])
    return neighbors_list, neighbors_coords_list


if __name__ == "__main__":
    with open(INPUT_FILE) as infile:
        lines_list = infile.read().splitlines()
    engine_accumulator = ""
    part1_total_parts_sum = 0
    is_part_number = False
    for row in range(len(lines_list)):
        for col in range(len(lines_list[row])):
            if lines_list[row][col].isnumeric():
                engine_accumulator += lines_list[row][col]
                neighbors_list, neighbors_coords_list = find_neighbors(col, row, lines_list)
                for char in range(len(neighbors_list)):
                    if (not neighbors_list[char].isnumeric()) and neighbors_list[char] != ".":
                        is_part_number = True

            else:
                if is_part_number:
                    part1_total_parts_sum += int(engine_accumulator)
                    # print(engine_accumulator, "added to total of", total_parts_sum)
                engine_accumulator = ""
                is_part_number = False
            # print(engine_accumulator)

    print("Part 1:", part1_total_parts_sum)

    for row in range(len(lines_list)):
        for col in range(len(lines_list[row])):
            if lines_list[row][col] == "*":
                neighbors_list, neighbors_coords_list = find_neighbors(col, row, lines_list)
