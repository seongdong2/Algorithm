#묶음을 찾아주는 프로그램은 DFS를 이용하면 간단하게 해결할 수 있다.
n, m = map(int, input().split())

gragh = []
for _ in range(n) :
    gragh.append(list(map(int, input())))


def dfs(x, y) :
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False

#0인 지점 하나를 찾아서 좌표 별로 T/F 부여
#재귀를 통해 기준점부터 깊이 탐색
    if gragh[x][y] == 0 :
        gragh[x][y] == 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

rst = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True :
            rst +=1


                


