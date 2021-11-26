#약수의 갯수가 홀수인 경우는 제곱수인 경우 뿐이다.
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if isEven(i) : answer +=1
        else :answer -= 1
    return answer

#1/2 제곱수가 정수면 > 홀수의 약수 갯수를 가지게 됌.
def isEven(num):
    return True if (num**(1/2))%1 > 0 else False