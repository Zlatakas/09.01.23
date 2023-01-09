a = int(input("введите число"))
b = int(input("введите число"))
if a == b:
    print(a)
else:
    for i in range(a, b + 1, 1):
        print(i, end=" ")

    for i in range(a, b - 1, -1):
        print(i, end=" ")