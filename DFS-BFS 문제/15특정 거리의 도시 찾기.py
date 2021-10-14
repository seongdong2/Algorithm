n, m, k, x = map(int, input().split())
visited = [False]*9

array = []
for _ in m :
    array.append(map(int, input().split()))


def dfs(array, x, visited):
    visited[x] = True
    for i in array[x]:
        if not visited[i]:
            dfs(array, i, visited)



