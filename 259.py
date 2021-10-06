Inf = int(1e9)

n, m = map(int, input().split())

gragh = [[Inf]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            gragh[a][b]== 0

for _ in range(m) :
    a, b= map(int,input().split())
    gragh[a][b] == 1

x, k = map(int,input().split())

for k in range(n+1):
    for a in range(n+1):
        for x in range(n+1):
            gragh[a][x] = min(gragh[a][x], gragh[a][k]+gragh[k][x])

print(gragh[a][x])