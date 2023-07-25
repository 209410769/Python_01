# Python Compound Interest Calculator
# 總金額 = 本金 * (1 +(利率 / 100)) ** 時間
def amount():
    amount = 0
    while amount <= 0:
        amount = float(input("請輸入本金金額:"))
        if amount <= 0:
            print("本金金額不能小於或是等於零")
    return amount


def rate():
    rate = 0
    while rate <= 0:
        rate = float(input("請輸入利率"))
        if rate <= 0:
            print("利率不能小於或等於零")
    return rate


def time():
    time = 0
    while time <= 0:
        time = int(input("請輸入年限："))
        if time <= 0:
            print("年限不能小於或等於零")
    return time


amount = amount()
rate = rate()
time = time()
total = amount*(1+(rate/100))**time

print("本金:", amount)
print("利率:", rate)
print("年限:", time)
print("淨利:", total)
print("扣除本金", total-amount)
