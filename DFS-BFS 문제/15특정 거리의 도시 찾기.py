#모든 거리가 1이기 때문에 너비 탐색을 시작한다
from collections import deque


#도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())

#A에서 B로 이동하는 단반향 도로 존재
p = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    p[a].append(b)

distance = [-1]*(n+1)
distance[x] = 0

q=deque([x])
while q :
    now = q.popleft()
    for next_node in p[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)



for i in range(n):
    if distance[i] == k:
        rst

print(rst)