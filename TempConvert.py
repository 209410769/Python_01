# python Temperature Convert
unit = input("請輸入當前的溫度單位（攝氏 C,華氏 F)").upper()
temp = float(input("請輸入溫度"))

if unit == 'C':
    temp = round(9*temp/5+32)
    print(f'當前的溫度為{temp}度F')
elif unit == 'F':
    temp = round((temp-32)*5/9)
    print(f'當前的溫度為{temp}度C')
else:
    print("非法溫度單位")
