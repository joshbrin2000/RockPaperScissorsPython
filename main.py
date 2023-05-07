import random
from enum import Enum


class RPS(Enum):
    rock = 1
    paper = 2
    scissors = 3


def compMove():
    choice = random.randint(1,3)
    choiceStr = RPS(choice).name
    print(f"Computer input is: {choiceStr}")
    return choice


def compare(r1, r2):
    if r1 == r2:
        print("tie")
        return None
    elif (r1 == 1 and r2 == 2) or (r1 == 2 and r2 == 3) or (r1 == 3 and r2 == 1):
        print(f"{RPS(r2).name} beats {RPS(r1).name}")
        return r2
    else:
        print(f"{RPS(r1).name} beats {RPS(r2).name}")
        return r1

def main():
    print("ROCK-PAPER-SCISSORS")
    print("Enter your choice: Rock, Paper, or Scissors")
    resultStr = input().lower()
    result = RPS[resultStr].value
    print(f"Player input is: {resultStr}")
    compResult = compMove()
    winner = compare(compResult, result)
    if winner == result:
        print("Player wins")
    elif winner == compResult:
        print("Computer wins")


if __name__ == "__main__":
    main()