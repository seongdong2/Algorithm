n = int(input())

#사과 갯수 && 사과 행렬 위치
k = int(input())
k_array=[]
for i in range(k) :
    k_array.append(map(int,input().split()))

#뱀 방향 변환 횟수 && 방향 변환 횟수 및 방향
l = int(input())
l_array = []
for i in range(l):
    l_array.append(map(int,input().split()))


map = [[0]*n for _ in range(n)]


