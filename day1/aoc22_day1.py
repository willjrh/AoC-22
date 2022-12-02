from pathlib import Path
from itertools import groupby


def main():
    input_file = Path() / "day1_in.txt"
    with open(input_file) as file:
        lines = [line.rstrip() for line in file]

    split_lists: list[list[str]] = split_list(lines)
    # part 1
    print(f"Part 1: {max(sum_list(split_lists))} calories")

    # part 2
    print(f"Part 2: {sum(sorted(sum_list(split_lists))[-3:])} calories")


def split_list(l: list):
    return [list(sub) for ele, sub in groupby(l, key=bool) if ele]


def sum_list(l_2d: list[list[str]]):
    return [sum(map(int, l)) for l in l_2d]


if __name__ == "__main__":
    main()
