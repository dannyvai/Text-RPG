import sys
from data.battle import enemy_gen
from data.myinput import myinput

sys.setrecursionlimit(10**6)  # test


def events(character):
    if character.location == "d3":
        if character.d3_event_4:
            print("In the distance you see a man sitting down in the grass staring at you, maybe you should\n"
                  "go talk to him.")
            myinput(">...")
            event_check(character)
    if character.location == "d4":
        if character.d4_event_1:
            print("As you enter the forest, you feel as if you are being watched by something.")
            myinput(">...")
            enemy_gen(character)
    if character.location == "d5":
        if character.d5_event_1:
            print("As you walk back into the forest again, you see the strange man hiding, rather poorly, behind a bush.\n"
                  "If you want your gold back you should go and talk to him.")
            myinput(">...")
            event_check(character)
    if character.location == "f6":
        if character.f6_event_2:
            print("As you walk towards the river you hear something run up from behind you.")
            myinput(">...")
            enemy_gen(character)
    if character.location == "g6":
        if character.g6_event_2:
            print("You start to swim across the river, but suddenly feel your leg being pulled from beneath you.")
            myinput(">...")
            enemy_gen(character)
    if character.location == "k6":
        if character.k6_event_2:
            print("You arrive onto dry land again, but it's not long before you are interrupted again.")
            myinput(">...")
            enemy_gen(character)
    if character.location == "o7":
        if character.o7_event_2:
            print("You find a torch on the wall and decide to light it so you can see what's in the dungeon, but now what's\n"
                  "in the dungeon can see you as well!")
            myinput(">...")
            enemy_gen(character)
    if character.location == "q10":
        if character.q10_event_1:
            print("Close to the end now, you prepare yourself for your battle against the Baron of Hell, but you are\n"
                  "ambushed when doing so.")
            myinput(">...")
            enemy_gen(character)


def event_check(character):
    if character.location == "d3":
        if character.d3_event_4:
            character.d3_event_4 = False
    if character.location == "d4":
        if character.d4_event_1:
            character.d4_event_1 = False
    if character.location == "d5":
        if character.d5_event_1:
            character.d5_event_1 = False
    if character.location == "f6":
        if character.f6_event_2:
            character.f6_event_2 = False
    if character.location == "g6":
        if character.g6_event_2:
            character.g6_event_2 = False
    if character.location == "k6":
        if character.k6_event_2:
            character.k6_event_2 = False
    if character.location == "o7":
        if character.o7_event_2:
            character.o7_event_2 = False
    if character.location == "q10":
        if character.q10_event_1:
            character.q10_event_1 = False

