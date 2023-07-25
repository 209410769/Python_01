# Python Caclulator
operator = input('請輸入運算符(+,-,*,/)')
num1 = float(input("請輸入一個數字"))
num2 = float(input("請輸入一個數字"))

if operator == '+':
    result = num1+num2
elif operator == '-':
    result = num1-num2
elif operator == '*':
    result = num1*num2
elif operator == '/':
    result = num1/num2
else:
    print("請輸入正確的運算符號")
print(result)
