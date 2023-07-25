menu = {
    "Pizza" : 300,
    "Popcorn" : 200,
    "french fries" : 90,
    "potato chips" : 60,
    "soft bread sticks" : 120, 
    "Soda" : 60,
    "lemon water" : 90 
}

cart = []
total = 0
print("菜單")
print("----------")
for item, price in menu.items():
    print(f"{item}:{price}")

while True:
    food = input("請輸入餐點(輸入q結束)")
    if food== "q":
        break
    elif menu.get(food) is None:
        print("查無此項目")
    else:
        cart.append(food)
        total +=menu.get(food)
        print(food,end=" ")
print(f"總共{total}元")