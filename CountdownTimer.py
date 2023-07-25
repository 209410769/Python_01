# Python Countdown Timer
import time
my_time = int(input("請輸入秒數:"))
for x in range(my_time, 0, -1):
    senonds = x % 60
    minutes = x // 60 % 60
    print(f"{minutes:02}:{senonds:02}")
    time.sleep(1)
print("times up")
