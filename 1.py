a = []
minMat = []

for i in range(20):
    b = int(input())
    a.append(b)
print(a)



for i in a:
    if (i % 2 == 0) and (i % 3 == 0):
        minMat.append(i)

minVal = minMat[0]


for j in minMat:
    if j <= minVal:
        minVal = j

print(minVal)

