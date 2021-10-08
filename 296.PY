from collections import deque

v, e = map(int, input().split())

#모든 노드에 대한 진입차수는 0
indegree = [0]*(v+1)

#각 노드에 연결된 간선 정보를 담기 위해 연결 리스트 초기화
gragh = [[] for i in range(v+1)]

#노드 별 관계를 저장하고, 관계가 규정된 경우 노드 액션이 발생했다는 말이니까, indegree +1
for _ in range(e):
    a, b = map(int, input().split())
    gragh[a].append(b)
    indegree[b] += 1

def to():
    result = []
    q = deque()

    #간선이 0인 노드이면, q에 i 삽입
    for i in range(1, v+1):
        if indegree[i] == 0 :
            q.append(i)

    while q:
        #큐에서 노드 꺼내기
        now = q.popleft()
        result.append(now)

        #해당 원소와 연결된 노드들의 진입차수 1 빼기
        for i in gragh[now]:
            indegree[i] -= 1
            if indegree[i] == 0 :
                q.append[i]

    for i in result :
        print(i, end = ' ')

to()
