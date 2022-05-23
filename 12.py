import random

n = 28
a = []
minVal = 100

for i in range(n):
    a.append(random.randint(0, 100))

for j in a:
    if j > 40 and j <= minVal:
        minVal = j

print(minVal)

