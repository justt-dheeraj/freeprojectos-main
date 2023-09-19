import os
import time
import utils

utils.cls()

print("""
[1] Houge
[2] Ticktacktoe
[3] Snake Game.
""")


while True:
    game_select = input(str("[?]: "))

    if game_select == '1':
        utils.cls()
        os.startfile("Houge.py")
        break

    elif game_select == '2':
        utils.cls()
        os.startfile("ticktacktoe.py")
        break

    elif game_select == '3':
        os.startfile("home.py")
        os.startfile("snake.py")
        exit()

    else:
        print("Invaild option!")