import random

n = 40
a = []
j = 0
k = 0

for i in range(n):
    a.append(random.randint(-100, 100))

print(a)

for i in range(n):
    if a[i] > 0:
        j += 1
        if j == 3:
            k = i


if j >= 3:
    print(k)
else:
    print("Меньше 3 полож элементов")




