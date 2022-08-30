from typing import Iterable, List
from random import randint


def parse_integer(num_string: str, choice: Iterable,) -> int:
    """
    Return the 'num_string' as an integer before validating it.

    The 'choice' is iterator of expected integer values.
    """
    try:
        num = int(num_string.strip())
    except ValueError:
        raise ValueError(f"{num_string} is not a integer.")
    else:
        if num in choice:
            return num
        else:
            raise ValueError(f"Expecting the value in {choice}, but got {num}")


def roll(ndices: int) -> List[int]:
    """
    Return a list of integers with length of 'ndices'.

    Each integer in the returned list is a random number between 1 and 6, inclusive.
    """
    roll_results = []
    for _ in range(ndices):
        roll_results.append(randint(1, 6))

    return roll_results


def display_dice_face_diagram(dice_values: List[int]) -> None:
    """
    Print an ASCII diagram of dice faces from `dice_values`.

    The string contains an ASCII representation of each die.
    For example, if 'dice_values = [4, 1, 3, 2]' then the string
    looks like this:

    ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
    │  ●   ●  │ │         │ │  ●      │ │  ●      │
    │         │ │    ●    │ │    ●    │ │         │
    │  ●   ●  │ │         │ │      ●  │ │      ●  │
    └─────────┘ └─────────┘ └─────────┘ └─────────┘
    """
    dice_art = {
        1: ("┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘",),
        2: ("┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘",),
        3: ("┌─────────┐", "│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘",),
        4: ("┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘",),
        5: ("┌─────────┐", "│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘",),
        6: ("┌─────────┐", "│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │", "└─────────┘",),
    }

    dice_faces = []
    for value in dice_values:
        dice_faces.append(dice_art[value])
    for row in zip(*dice_faces):
        for one in row:
            print(one, end=' ')
        print()

def main():
    """Starting point for the program."""
    ndices = parse_integer(
        input("How many dice do you want to roll? [1-6]: "), range(1, 7)
    )
    values = roll(ndices)
    display_dice_face_diagram(values)


if __name__ == "__main__":
    main()
