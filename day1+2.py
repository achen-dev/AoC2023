# This is the driver code for the 2023 AoC event

def day_one(input_file):
    with open(input_file) as infile:
        lines_list = infile.read().splitlines()
    # print(lines_list)

    # Part 1:
    part1_total_sum = 0

    for line in lines_list:
        line_digits = []
        for char in line:
            if char.isnumeric():
                line_digits.append(char)
        # print(line_digits)
        if line_digits:
            line_sum = int(line_digits[0] + line_digits[-1])
            part1_total_sum += line_sum
    print("Part 1 Total Sum:", part1_total_sum)

    # Part 2:
    part2_total_sum = 0
    char_dig_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    for line in lines_list:
        line_digits = []
        char_accumulator = ""
        for char in line:
            if char.isnumeric():
                line_digits.append(char)
            else:
                char_accumulator += char
                for char_key in char_dig_dict:
                    if char_key in char_accumulator:
                        line_digits.append(str(char_dig_dict[char_key]))  # Hacky solution to avoid rewriting dict
                        char_accumulator = char
                    else:
                        continue

        line_sum = int(line_digits[0] + line_digits[-1])
        part2_total_sum += line_sum
    print("Part 2 Total Sum:", part2_total_sum)


def day_two(input_file):
    with open(input_file) as infile:
        lines_list = infile.read().splitlines()

    # Part 1
    RED_LIMIT = 12
    GREEN_LIMIT = 13
    BLUE_LIMIT = 14

    total_id_sum = 0
    total_power_sum = 0  # Part 2 sum
    for line in lines_list:
        line_list = line.split(" ")
        game_id = line_list[1][:-1]

        max_red = 0
        max_green = 0
        max_blue = 0
        for i in range(len(line_list)):
            if "red" in line_list[i]:
                if int(line_list[i-1]) > max_red:
                    max_red = int(line_list[i-1])
            elif "green" in line_list[i]:
                if int(line_list[i-1]) > max_green:
                    max_green = int(line_list[i-1])
            elif "blue" in line_list[i]:
                if int(line_list[i-1]) > max_blue:
                    max_blue = int(line_list[i-1])
        if max_red <= RED_LIMIT and max_green <= GREEN_LIMIT and max_blue <= BLUE_LIMIT:
            total_id_sum += int(game_id)

        # Part 2:
        power = max_red * max_green * max_blue
        total_power_sum += power

    print("Part 1 Total Sum:", total_id_sum)
    print("Part 2 Total Sum:", total_power_sum)


if __name__ == '__main__':
    print("Day 1:")
    day_one('inputs/day1')
    print("Day 2:")
    day_two("inputs/day2")
