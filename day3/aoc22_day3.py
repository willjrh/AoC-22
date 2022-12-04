from pathlib import Path


def split_string_half(string: str) -> tuple[str, str]:
    return string[: len(string) // 2], string[len(string) // 2 :]


def common_char(strings: tuple[str, str]):
    return list(set(strings[0]) & set(strings[1]))[0]


def common_char3(strings: list[str, str, str]):
    return list(set(strings[0]) & set(strings[1]) & set(strings[2]))[0]


def string_value(string: str) -> int:
    if string[0].isupper():
        return ord(string[0]) - ord("A") + 27
    else:
        return ord(string[0]) - ord("a") + 1


def main() -> None:
    input_file = Path() / "day3_in.txt"
    with open(input_file) as file:
        lines = [line.rstrip() for line in file]

    print(
        "Part 1:"
        f" {sum([string_value(common_char(split_string_half(l))) for l in lines])}"
    )

    total = 0
    for i in range(0, len(lines), 3):
        total += string_value(common_char3(lines[i : i + 3]))
    print(f"Part 2: {total}")


if __name__ == "__main__":
    main()
