#DFS
def dfs(gragh, start, visited):
    visited[start] = True
    for v in gragh[start] :
        #여기서 뭔가를 더 할 수 있음
        if not visited[v] :
            bfs(gragh, v, visited)

#BFS
from collections import deque
def bfs(gragh, start, visited):
    queue = deque([start])
    visited[start]= True
    while queue:
        v = queue.popleft()
        #여기서 뭔가를 더 할 수 있음
        for i in gragh[v]:
            if not visited[i] :
                queue.append(i)
                visited[i] = True



    
        
