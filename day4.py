INPUT_FILE = "inputs/day4"


if __name__ == "__main__":
    with open(INPUT_FILE) as infile:
        lines_list = infile.read().splitlines()

    part1_points_sum = 0
    for line in lines_list:
        card_num, num_list = line.split(":")
        winning_nums, my_nums = num_list.split("|")
        win_nums_list = [num for num in winning_nums.split(" ") if num != ""]
        my_nums_list = [num for num in my_nums.split(" ") if num != ""]

        match_count = -1
        for win_num in win_nums_list:
            for my_num in my_nums_list:
                if my_num == win_num:
                    match_count += 1

        if match_count != -1:
            line_sum = 2**match_count
            part1_points_sum += line_sum

    print("Part 1 points sum:", part1_points_sum)

    cards_list = []
    # Format cards in (card_num: int, winning_nums: list, my_nums: list, count:int)
    for line in lines_list:
        card_name, num_list = line.split(":")
        card_num = int(card_name.split(" ")[-1])
        winning_nums, my_nums = num_list.split("|")
        win_nums_list = [num for num in winning_nums.split(" ") if num != ""]
        my_nums_list = [num for num in my_nums.split(" ") if num != ""]
        cards_list.append([card_num, win_nums_list, my_nums_list, 1])

    part2_total_cards = 0
    for card in cards_list:
        for count in range(card[3]):
            part2_total_cards += 1
            match_count = 0

            for win_num in card[1]:
                for my_num in card[2]:
                    if my_num == win_num:
                        match_count += 1

            for i in range(match_count):
                cards_list[card[0]+i][3] += 1
        # print(cards_list)

    print("Part 2 cards sum:", part2_total_cards)