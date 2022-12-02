from pathlib import Path
from itertools import groupby


def main():
    input_file = Path() / "day1_in.txt"
    with open(input_file) as file:
        lines = [line.rstrip() for line in file]

    split_lists: list[list[str]] = split_list(lines)
    print(max(sum_list(split_lists)))

    # part 2
    print(sum(sorted(sum_list(split_lists))[-3:]))


def split_list(l: list):
    return [list(sub) for ele, sub in groupby(l, key=bool) if ele]


def sum_list(l_2d: list[list[str]]):
    totals = []
    for l in l_2d:
        totals.append(sum(map(int, l)))
    return totals


if __name__ == "__main__":
    main()
