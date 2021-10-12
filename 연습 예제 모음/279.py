def find(parent, x):
    if parent[x] != x :
        parent[x] =find(parent, parent[x])
    return parent[x]

def uni(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

v, e = map(int, input().split())
parent = [0]*(v+1)

for i in range(1, v+1) :    
    parent[i] = i

cycle = False

for i in range(e) :
    a, b = map(int, input().split())
    if find(parent, a) == find(parent, b) :
        cycle = True
    
    else : 
        uni(parent, a, b)

if cycle :
    print('사이클')
else :
    print('ㄴㄴ')