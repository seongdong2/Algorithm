#d[n] = max(d1[n-1], d2[n-1], d3[n-1])



#1차원 리스트를 2차원 리스트로 만들기
def make(array):
    mining = []
    count = 0
    for i in range(1, n+1):
        tmp = []
        for j in range(1, m+1):
            tmp.append(array[count])
            count += 1
        mining.append(tmp) 
    return mining


def dp(array):
    d= [[0] * 20 for i in range(20)]
    d[1][1] = 1
    d[1][2] = 2
    d[1][0] = 0
    #dp 를 다음부터 하면 됌





t = int(input())    
while True:
    if t == 0:
        break

    n, m = map(int, input().split())
    _list = list(map(int, input().split()))
    mining = make(_list)
    #딱 dp를 다음부터 하면 됌




    print()
    t -= 1


