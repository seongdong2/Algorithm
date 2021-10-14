#묶음을 찾아주는 프로그램은 DFS를 이용하면 간단하게 해결할 수 있다.
from collections import deque

def bfs(gragh, a, b, state) :
    q=deque([a][b])
    state[a][b] = 1

    while q : 
        for i in gragh[a] :
            if not state[a][i] != 1 :
                now = q.popleft()
                state[a][i] == 1
            q.append(q[a][i])
    return bfs(gragh, now[0], now[1], state)
        

                


