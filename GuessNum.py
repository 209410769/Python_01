# Python Guess Number
import random
low=1
high=100
number = random.randint(low,high)
guesses =0
error = 0
while True:
    # 讓玩家猜測數字
    guess = int(input(f"請輸入一個介於{low}~{high}之間的數字"))

    if (guess<low):
        print("超出範圍了，確認一下")
        error += 1
    elif (guess>high):
        print("超出範圍了，確認一下")
        error += 1
    else:
        if (guess>number):
            print("數字太大了 猜小一點")
            high = guess
            guesses += 1
        elif guess < number :
            print("數字太小了 猜大一點")
            low = guess
            guesses += 1
        else:
            guesses += 1
            print(f"恭喜花了{guesses}次答對，超出{error}次範圍")

            break