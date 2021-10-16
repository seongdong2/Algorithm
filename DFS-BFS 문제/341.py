#이 문제는 벽 3개 설치하는 모든 경우의 수를 다 계산해야 한다.


from collections import deque


def bfs(array, a,  )

n, m = map(int, input().spilt())

world = virus = []

#맵 열기
for i in range(n+1) :
    world.append(list(map(int, input().split())))

#바이러스 위치
for a in range(n+1) :
    for b in range(m+1) :
        if world[a][b] == 2 :
            virus.append(list(a,b))


q= deque(virus[0])
while q:
    
