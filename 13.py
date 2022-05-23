import random

n = 50
a = []
j = 0

for i in range(n):
    a.append(random.randint(-100, 100))

print(a)


for i in range(n):
    if a[i] < 0:
        j = i
        break

if j >= 0:
    print(j)

else:
    print("Отрицательного элемента нет")