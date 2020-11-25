import art
import game_data
import random
from prompt_toolkit.shortcuts.utils import clear

all_data = game_data.data.copy()
score = 0
play_again = True


def choose_obj():
    i = random.randint(0, len(all_data))
    data_obj = all_data[i]
    all_data.pop(i)
    return data_obj


def try_again():
    print("Wrong! Game Over.")
    request = input("Play again? Type 'y' to continue, type 'n' to exit: ")
    while request not in ['y', 'n']:
        request = input("'y' to continue, type 'n' to exit: ")
    if request == 'y':
        return True
    return False


while play_again or score >= 0:
    clear()
    print(art.logo)
    if score > 0:
        print(f"You are right! Current score: {score}")
        data_A = data_B.copy()
    else:
        all_data = game_data.data.copy()
        data_A = choose_obj()
        score = 0
    data_B = choose_obj()
    answer = 'b' if data_B['follower_count'] > data_A['follower_count'] else 'a'
    print(
        f"Compare A: {data_A['name']},  {data_A['description']}, from {data_A['country']}")
    print(art.vs)
    print(
        f"Compare B: {data_B['name']},  {data_B['description']}, from {data_B['country']}")
    choice = input("Who has more followers? Type 'A' or 'B': ")
    while choice not in ['A', 'a', 'B', 'b']:
        choice = input("Type 'A' or 'B': ")
    if choice.lower() == answer:
        score += 1
    else:
        score = -1
        play_again = try_again()
