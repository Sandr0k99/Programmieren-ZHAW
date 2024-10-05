import random
from enum import Enum


class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

options = [{"type": Choice.ROCK, "wins_against": Choice.SCISSOR},
           {"type": Choice.PAPER, "wins_against": Choice.ROCK},
           {"type": Choice.SCISSOR, "wins_against": Choice.PAPER}]

user_choice = int(input("Rock [1], Paper [2], Scissors[3] shoot: "))

comp_choice = random.choice(options)
comp_choice_name = comp_choice["type"].name

if Choice(user_choice) == comp_choice["type"]:
    print(f"Computer chooses {comp_choice_name}. TIE GAME!")
elif comp_choice["wins_against"] == Choice(user_choice):
    print(f"Computer chooses {comp_choice_name}. YOU LOSE!")
else:
    print(f"Computer chooses {comp_choice_name}. YOU WIN!")
