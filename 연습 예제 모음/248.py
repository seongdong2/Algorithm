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
        #최단거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappush(q)
        
        #현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist :
            continue

        for i in gragh[now]:
            cost = dist + i[1]

            #현재 노드를 거쳐서 다음 노드로 가는게, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                #정리하려는 게 아니라, 단순히 최단 거리로 계산된 cost값을 q의 i[0]번째 노드에 넣어주는 과정이다.
                heapq.heappush(q, (cost, i[0]))

di(start)

for i in range(1, n+1) :
    if distance[i] == Inf:
        print("INF")
    else:
        print(distance[i])


