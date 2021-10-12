s = list(map(int, input()))
rst = 0

for i in range(len(s)) :
    if s[i] == 0 or rst == 0:
        rst += s[i]
    else :
        rst *= s[i]

print(rst)

#아이디어 : 최대한 곱해줘야 크다
#0일 때 와 앞선 결과가 0일 때, 더하기를 해주고
#나머지는 곱하기를 해준다