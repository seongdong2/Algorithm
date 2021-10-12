Inf = int(1e9)
n = int(input())
m = int(input())
gragh = [[Inf]*(n+1) for i in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b :
            gragh[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    gragh[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            gragh[a][b] = min(gragh[a][b], gragh[a][k]+gragh[b][k])

for a in range(1, n+1):
    for b in range(1, n+1):
        