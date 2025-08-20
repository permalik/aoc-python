# main.py

import os


def main():
    one()
    two()


def one():
    dir_path = os.environ["DIR_PATH"]
    square_feet = 0
    with open(f"{dir_path}2015/002/input.txt", encoding="utf-8") as f:
        raw_data = f.read().replace("\n", "")

    print("RAW: ", raw_data)
    print("Santa is on floor: ", square_feet)


def two():
    dir_path = os.environ["DIR_PATH"]
    square_feet = 0
    with open(f"{dir_path}2015/002/input.txt", encoding="utf-8") as f:
        raw_data = f.read().replace("\n", "")

    print("RAW: ", raw_data)
    print(f"The elves need {square_feet} of wrapping paper")


if __name__ == "__main__":
    main()
