def dfs(array, x, visited):
    if 
    visited[x] = True
    for i in array[x]:
        if not visited[i]:
            dfs(array, i, visited)
        




n, m, k, x = map(int, input().split())
visited = [False]*n

array = []
for _ in m :
    array.append(map(int, input().split()))

dfs(array, x, visited)



