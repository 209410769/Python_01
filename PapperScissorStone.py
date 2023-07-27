import random

player = None
computer = None

running = True
options =["Papper","Scissor","Stone"]
win = 0
lose = 0
while running:
    player = input("Papper & Scissor & Stone:")
    while player not in options:
        input("Input error Please input Papper & Scissor & Stone:")
    computer = random.choice(options)
    print(f"Player:{player}，Computer:{computer}")
    if player == computer:
        print("Tie")
    elif player == "Scissor" and computer =="Papper":
        print("congratulations you win")
        win += 1
    elif player == "Stone" and computer =="Scissor":
        print("congratulations you win")
        win += 1
    elif player == "Papper" and computer =="Stone":
        print("congratulations you win")
        win += 1
    else:
        print("oops you lose")
        lose += 1

    play_again = input("再玩一局?(y/n)").lower()
    if not play_again == "y":
        running = False
print(f"Thanks for comming you got {win} times for win,{lose} times for lose")
