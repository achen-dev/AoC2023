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
    has_star_neighbor = False
    full_star_dict = {}
    star_coords_list = []
    for row in range(len(lines_list)):
        for col in range(len(lines_list[row])):
            if lines_list[row][col].isnumeric():
                engine_accumulator += lines_list[row][col]
                neighbors_list, neighbors_coords_list = find_neighbors(col, row, lines_list)
                for char in range(len(neighbors_list)):
                    if (not neighbors_list[char].isnumeric()) and neighbors_list[char] != ".":
                        is_part_number = True
                    if neighbors_list[char] == "*":
                        has_star_neighbor = True
                        if neighbors_coords_list[char] not in star_coords_list:
                            star_coords_list.append(neighbors_coords_list[char])

            else:
                if is_part_number:
                    part1_total_parts_sum += int(engine_accumulator)
                    # print(engine_accumulator, "added to total of", total_parts_sum)
                if has_star_neighbor:
                    print(engine_accumulator, "has a star")
                    print(star_coords_list)
                    for star in star_coords_list:
                        if star in full_star_dict:
                            full_star_dict[star].append(int(engine_accumulator))
                        else:
                            full_star_dict[star] = [int(engine_accumulator)]
                engine_accumulator = ""
                is_part_number = False
                has_star_neighbor = False
                star_coords_list = []
            # print(engine_accumulator)
    print(full_star_dict)
    part2_total_gear_sum = 0
    for star in full_star_dict:
        if len(full_star_dict[star]) == 2:
            part2_total_gear_sum += full_star_dict[star][0]*full_star_dict[star][1]

    print("Part 1:", part1_total_parts_sum)
    print("Part 2:", part2_total_gear_sum)