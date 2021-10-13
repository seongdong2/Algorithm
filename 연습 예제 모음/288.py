def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def uni(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b :
        parent[b] = a
    else : 
        parent[a] = b

v, e = map(int, input().split())
parent = [0]*(v+1)

for i in range(1, v+1) :
    parent[i] = i


#모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges =[]
result = 0


for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append(cost, a, b)

#간선을 비용이 적은 순으로 정리
edges.sort()

#간선을 확인하면서
for edge in edges :
    cost, a, b, = edge
    #루트 노드값이 다른 경우만 유니 적용, 신장트리, 사이클 발생하지 않도록 구조 완성
    if find(parent, a) != find(parent, b) :
        uni(parent, a, b)
        result += cost
    

print(result)