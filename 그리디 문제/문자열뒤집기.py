# 전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우 중에 더 적은 횟수를 가진 경우를 계산한다.

s = list(map(int, input()))
cnt = 0
rst1 = 0
rst2 = 0

for i in range(len(s)) :
    if s[i] and s[i-1] == 1 : 
        rst1 += 1
    elif s[i] and s[i-1] == 0:
        rst2 += 1
    else :
        continue
        
for i in range(len(s)) :
        if s[i-1] :
            if s[i] != s[i-1] :
                cnt += 1


if rst1 > rst2 :
    print(cnt)
else :
    print(cnt)
