N, M = map(int, input().split())
d = [[0]*M for i in range(N)]


A, B, d = map(int, input().split())
d[A][B] = 1

array = []
for i in range(N) :
    array.append(list(map(int, input().split())))

#북 동 남 서 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def t() :
    global dir
    dir -= 1
    if dir == -1 :
        dir ==3

count = 1 



    

