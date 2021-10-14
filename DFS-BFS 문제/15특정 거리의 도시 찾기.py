#'모든 도로의 거리가 1'이라는 조건 덕분에 너비 우선 탐색을 이용하여 간단히 해결할 수 있다.

from collections import deque

n, m, k, x = map(int, input().split())
gragh = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    gragh[a].append(b)

#모든 도시에 대한 최단 거리 초기화

distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])

while q :
    now = q.popleft()
    for next_node in gragh[now] :
        if distance[next_node] == -1 :
            #최단 거리 갱신
            distance[next_node] == distance[now] + 1
            q.append(next_node)

check = False
for i in range(1, n+1):
    if distance[i] == k :
        print(i)
        check = True

if check == False :
    print(-1)





