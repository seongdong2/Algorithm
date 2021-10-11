s = list(map(int, input()))
rst = 0

for i in range(len(s)) :
    if s[i] == 0 or rst == 0:
        rst += s[i]
    else :
        rst *= s[i]

print(rst)

#112 > 
#11112 
#1222222
#2222
#