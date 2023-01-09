#for i in range(10):
    #print("Иди вперед")
    #print(i)

a = int(input("введите число"))
b = int(input("введите число"))
for i in range(a, b+1):
    print(i, end=" ")

print(*range(1, 100, 5))
