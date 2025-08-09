# main.py


def main():
    one()


def one():
    current_floor = 0
    with open("/home/parallels/Docs/Git/aoc/2015/001/input.txt", encoding="utf-8") as f:
        raw_data = f.read().replace("\n", "")

    chars = list(raw_data)
    for char in chars:
        if char == "(":
            current_floor += 1
        elif char == ")":
            current_floor -= 1
        else:
            print("Invalid floor counter.")

    print("Santa is on floor: ", current_floor)


def two():
    print("running two.." + "\n\nd")


if __name__ == "__main__":
    main()
