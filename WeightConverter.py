# python Weight Converter
weight = float(input("請輸入您的體重:"))
unit = input("您的體重是公斤還是磅?(kg/lb)").upper()

if unit == 'KG':
    weight *= 2.2
    new_unit = '磅'
elif unit == 'LB':
    weight /= 2.2
    new_unit = '公斤'
else:
    print('單位不正確')
    exit()
print(f'您的體重是{round(weight)}{new_unit}')
