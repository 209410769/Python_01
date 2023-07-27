import random

# randint()

# print(random.randint(1,10))

# random()

# print(random.random())

# 列表中隨機選擇一個元素

# options = ["剪刀","石頭","布"]
# rand_option = random.choice(options)
# print(rand_option)

#將一個列表打亂

cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
random.shuffle(cards)
print(cards)