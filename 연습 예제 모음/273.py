#부모 노드로 루트까지 빠르게 찾아 내기
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

#노드의 부모노드 통합/갱신하기
def uni_parent(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b :
        parent[b] = a
    else : 
        parent[a] = b

#노드의 개수와 간선(union 연산)의 개수
v, e = map(int, input().split())
parent = [0]*(v+1)

#노드 모두 자기자신을 부모 노드로 설정
for i in range(v+1):
    parent[i]=i

#a, b 는 뭘까?
for i in range(e):
    a, b = map(int, input().split())
    uni_parent(parent, a, b)

#각 원소가 속한 집합
print('각 원소가 속한 집합', end=' ')
for i in range(1, v+1):
    print(find(parent, i), end=' ')

print()




