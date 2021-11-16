a= ['hong', 'gil', 'dong']
b= []
c= {}
def enu(a, b, c):
    for i, name in enumerate(a):
        b.append([i,name])
        c[i]=b[i][1]

enu(a,b,c)

print(a)
print(b)
print(c)