# a = (i * 2 for i in range(0, int(input("Введи число: "))))
# for i in a:
#     print(i)

def even_numbers(*args, **kwargs):
    for i in range(0, int(input("Введите число: "))):
        yield i


for x in even_numbers():
    if x % 2 == 0:
        print(x)
    else:
        print("не число")
