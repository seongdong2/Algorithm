def find(parent, x):
    if parent[x] != x :
        parent[x] = find(parent, parent[x])
    return parent[x]

def uni(parent, a, b) :
    a = find(parent, a)
    b = find(parent, b)
    if a > b :
        parent[a] = parent[b]
    else :
        parent[b] = parent[a]
    
n, v = map(int, input().split())
parent = [0]*(n+1)

for i in range(0, n+1):
    parent[i] = i

array = []
result = 0

for i in range(v) :
    a, b, cost = map(int, input().split())
    array.append(cost, a, b)

array.sort()

for i in array :
    cost, a, b = i
    if find(parent, a) != find(parent, b):
        uni(parent, a, b)
        result += cost
        last 
