import random

n = 40
a = []
minVal = 100

for i in range(n):
    a.append(random.randint(-100, 100))

print(a)

for i in range(n):
    if a[i] >= 0 and a[i] <= minVal:
        minVal = a[i]


if minVal < 100:
    print(minVal)

else:
    print("Положительных нет")