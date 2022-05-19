a = []
c = []
n = 30
for i in range(n):
    b = int(input())
    a.append(b)

for i in a:
    if i >= 0:
        c.append(i)

print(sum(c))
    
