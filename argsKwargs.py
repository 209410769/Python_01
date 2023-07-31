# args => arguments 任意數量的參數 * => tuple
# def add(*args):
#     total = 0
#     for arg in args:
#         print(f"args:{arg}")
#         total+=arg
#     return total
# print(add(1,2,3))
# kwargs => 關鍵字 + args(keyword args)** => dictionary
# def print_info(**kwargs):
#     for key,value in kwargs.items():
#         print(f"key:{key} value:{value}")
# print_info(name="Alice",age="25",occupation="工程師")