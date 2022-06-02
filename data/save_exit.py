import os
import pickle
import sys
from data.myinput import myinput


def save(character, en1):
    from data.menu import game_menu
    if os.path.exists("save_file"):
        print("Are you sure you want to overwrite your current save? Y/N")
        option = myinput("> ")
        if option.lower() == "y":
            with open('save_file', 'wb') as f:
                pickle.dump(character, f)
                print("Game has been saved.")
        else:
            print("Game hasn't been saved.")
    else:
        with open('save_file', 'wb') as f:
            pickle.dump(character, f)
            print("Game has been saved.")
    myinput(">...")
    game_menu(character, en1)


def auto_save(character):
    with open('save_file', 'wb') as f:
        pickle.dump(character, f)


def exit_check(character, en1):
    from data.menu import game_menu
    from main import title_screen_selection
    os.system("cls")
    print("Are you sure you want to exit? Make sure you have saved first. Y/N")
    choice = myinput("> ")
    if choice.lower()[0] == "y":
        title_screen_selection(character, en1)
    else:
        game_menu(character, en1)
