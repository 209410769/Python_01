# for 迴圈
for i in range(1, 11):
    print(i)

for i in reversed(range(1, 11)):
    print(i)
print("Happy New Year!")

credit_card = "1234-5678-9012-3456"
for x in credit_card:
    if x == '9':
        # continue
        break
    else:
        print(x)

# 字典 dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
for x in my_dict:
    print(x)
for key, value in my_dict.items():
    print("key", key)
    print("value", value)
