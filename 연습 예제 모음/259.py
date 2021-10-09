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
    gragh[b][a] == 1
    #오고가는 정보이기 때문에 각각 1을 설정해줘야한다.

x, k = map(int,input().split())

#점화식에 따라 플로이드 워셜 알고리즘 수행하여, 행렬 완성
for k in range(n+1):
    for a in range(n+1):
        for x in range(n+1):
            gragh[a][x] = min(gragh[a][x], gragh[a][k]+gragh[k][x])

#문제에서 원했던 답 출력 > k를 들렸다가 x를 가는 최단 거리
distance = gragh[1][k]+ gragh[k][x]
if distance >= Inf :
    print('-1')

#도달할 수 있다면, 최단거리
else: 
    print(distance)