"""A tiny script for practicing the Claude -> GitHub -> Visual Studio round trip."""

from datetime import datetime

# Try changing these, then commit and push your edit!
NAME = "world"
FAVORITE_NUMBER = 7


def greet(name: str) -> str:
    hour = datetime.now().hour
    if hour < 12:
        part_of_day = "morning"
    elif hour < 18:
        part_of_day = "afternoon"
    else:
        part_of_day = "evening"
    return f"Good {part_of_day}, {name}!"


if __name__ == "__main__":
    print(greet(NAME))
    print(f"Your favorite number squared is {FAVORITE_NUMBER ** 2}.")
