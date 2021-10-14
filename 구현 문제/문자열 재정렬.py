n = input()
length = len(n)

a = []
b = 0

for i in range(length) : 
    if type(n[i]) is str :
        a.append(ord(n[i]))
    else : 
        print(n[i])
        b += int(n[i])

print(a)
print(b)


