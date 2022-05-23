import random

n = 40
a = []


for i in range(n):
    a.append(random.randint(-100, 100))

print(a)

maxVal = a[0]
maxVal1 = a[0]

for i in range(n):
    if a[i] >= maxVal:
        maxVal = a[i]

k = maxVal

for i in range(n):
    if a[i] >= maxVal1 and a[i] < k:
        maxVal1 = a[i]

print(maxVal1)



