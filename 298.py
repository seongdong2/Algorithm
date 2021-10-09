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

n, m = map(int, input().split())
parent = [0]*(n+1)

for i in (0, n+1) :
    parent[i] = i

for i in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0 :
        uni(parent, a, b)
    elif oper == 1 :
        if find(parent, a) == find(parnet, b):
            print('yes')
        else : 
            print('no')