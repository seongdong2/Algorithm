import heapq
import sys
input = sys.stdin.readline
Inf = int(1e9)

n, m = map(int, input().split())

start = int(input())

gragh= [[] for i in range(n+1)]

distance = [Inf] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    gragh[a].append(b,c)


def di(start):
    q= []
    heapq.heappush(q, (0, start))
    distance[start]=0
    while q:
        dist, now = heapq.heappush(q)
        if distance[now] < dis :
            continue

        for i in gragh[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

di(start)

for i in range(1, n+1) :
    if distance[i] == Inf:
        print("INF")
    else:
        print(distance[i])


