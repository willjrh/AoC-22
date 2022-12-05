from pathlib import Path


def main() -> None:
    input_file = Path() / "day4_in.txt"
    with open(input_file) as file:
        lines = [line.rstrip() for line in file]

    full_captured: list[bool] = [fully_captured(l) for l in lines]
    partial_captured: list[bool] = [partially_captured(l) for l in lines]
    print(f"Part 1: {sum(full_captured)}")
    print(f"Part 2: {sum(partial_captured)}")


def fully_captured(code: str) -> bool:
    first, second = code.split(",")
    first_lower, first_upper = first.split("-")
    second_lower, second_upper = second.split("-")
    if int(first_lower) <= int(second_lower) and int(first_upper) >= int(second_upper):
        return True
    elif int(second_lower) <= int(first_lower) and int(second_upper) >= int(
        first_upper
    ):
        return True
    else:
        return False


def partially_captured(code: str) -> bool:
    first, second = code.split(",")
    first_lower, first_upper = first.split("-")
    second_lower, second_upper = second.split("-")
    first_set: set = set(range(int(first_lower), int(first_upper) + 1))
    second_set: set = set(range(int(second_lower), int(second_upper) + 1))
    if len(first_set & second_set) == 0:
        return False
    else:
        return True


if __name__ == "__main__":
    main()
