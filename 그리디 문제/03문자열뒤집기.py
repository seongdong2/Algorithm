# 전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우 중에 더 적은 횟수를 가진 경우를 계산한다.

s = input()
rst0 = 0 #전부 0으로 바꾸는 경우
rst1 = 0 #전부 1로 바꾸는 경우

#첫 번째 원소처리
if s[0] =='1':
    rst0 += 1
else : 
    rst1 += 1

#두 번째 원소로부터 모든 원소 확인
for i in range(len(s)-1) :
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            rst0 += 1
        else :
            rst1 += 1

print(min(rst0, rst1))