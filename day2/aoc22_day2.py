from pathlib import Path


def main():
    input_file = Path() / "day2_in.txt"
    inputs = [x.strip().split(" ") for x in open(input_file).readlines()]
    # part 1
    print(f"Part 1: {sum([part1(res) for res in inputs])}")
    # part 2
    print(f"Part 2: {sum([part2(res) for res in inputs])}")


def part1(game: list[str, str]):
    result: int = ord(game[0]) - ord("A") - ord(game[1]) + ord("X")
    play_bonus = ord(game[1]) - ord("X") + 1
    win = 6
    draw = 3
    loss = 0
    if result == 0:
        return play_bonus + draw
    if abs(result) == 1:
        if result > 0:
            return play_bonus + loss
        else:
            return play_bonus + win
    if abs(result) == 2:
        if result < 0:
            return play_bonus + loss
        else:
            return play_bonus + win


def part2(game: list[str, str]):
    result_dict = {"X": 0, "Y": 3, "Z": 6}
    bonus_dict = {
        "X": ((ord(game[0]) - ord("A") - 1) % 3) + 1,
        "Y": ord(game[0]) - ord("A") + 1,
        "Z": ((ord(game[0]) - ord("A") + 1) % 3) + 1,
    }
    return result_dict[game[1]] + bonus_dict[game[1]]


if __name__ == "__main__":
    main()


#
# A - X draw -> 0
# A - Y win -> -1
# A - Z loss -> -2
# B - X loss-> 1
# B - Y draw -> 0
# B - Z win -> -1
# Z - X win -> 2
# Z - Y loss -> 1
# Z - Z draw -> 0
# -2 loss
# -1 win
# 0 draw
# 1 loss
# 2 win

# ((ord(fisrt col) - ord("A") + 1) mod 3) + 1
