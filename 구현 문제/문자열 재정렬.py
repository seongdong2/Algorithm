data = input()
rst = []
v = 0

for i in data : 
    if i.isalpha() :
        rst.append(i)
    else : 
        v += int(i)

rst.sort()

if v != 0 :
    rst.append(str(v))

print(''.join(rst))

