import sys
input = sys.stdin.readline
Inf = int(1e9)

n, m = map(int, input().split())
#노드의 갯수, 간선의 개수를 입력받기

start = int(input())
#시작 노드 번호를 입력받기

gragh = [[] for i in range(n+1)]
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기

visited = [False] * (n+1)
#방문한 적이 있는지 체크하는 목적의 리스트 만들기
#우선큐와 다른 부분 

distance = [Inf]*(n+1)
#최단 거리 테이블을 모두 무한으로 초기화

#모든 간선 정보 입력받기 
for _ in range(m) :
    a, b, c = map(int, input().split())
    #a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    gragh[a].append((b, c))

#방문하지 않은 노드 중에, 가장 최단 거리가 짧은 노드 번호를 반환
def get_smallest_node():
    min_value = Inf
    index = 0 # 가장 최단 거리가 짧은 노드
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def di(start):
    distance[start] =0
    #시작 노드에 대해서 초기화
    
    visited[start] = True
    #distance의 a노드에서 b노드까지가는 거리 값
    for j in gragh[start] :
        distance[j[0]] = j[1]

    #시작한 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True

        #현재 노드와 연결된 다른 노드를 확인
        for j in gragh[now]:
            cost = distance[now] + j[1]

            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


