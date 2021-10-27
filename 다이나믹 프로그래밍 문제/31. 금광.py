for tc in range(int(int())):
    n, m = map(int, input().split())
    _list = list(map(int, input().split()))

    dp = []
    index = 0

    #1차원 리스트를 2차원 리스트로 만들기
    for i in range(n):
        dp.append(_list[index:index + m])
        index += m
    
    #dp
    for j in range(1, m):
        for i in range(n):
            #왼쪽 위
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            
            #왼쪽 아래
            if i == n-1:
                left_donw = 0
            else :
                left_down = dp[i+1][j-1]
            
            #왼쪽
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left, left_up, left_down)
    #다 저장된 정보 중에 최대 수를 고른다
    rst =0
    for i in range(n):
        rst = max(rst, dp[i][m-1])

    print(rst)


