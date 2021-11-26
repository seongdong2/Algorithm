#피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

def solution(n):
    answer = 0
    answer = fibo(n)%1234567
    print(fibo(n))
    return answer

def fibo(n):
    d=[0]*10000001
    d[1] = 1
    d[2] = 1
    for i in range(3, n+1) :
        d[i]=d[i-1]+d[i-2]
    return d[n]