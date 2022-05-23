import random

n = 30
a = []
j = 0

for i in range(n):
    a.append(random.randint(-100, 100))

print(a)

x = int(input())

for i in range(n):
    if a[i] == x:
        j = i
        break

if j >= 0:
    print(j)

else:
    print("Нет такого элемента")

