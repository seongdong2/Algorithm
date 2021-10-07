n, m = map(int,input().split())

f= [0]*100001

d = []
for _ in range(n):
    d.append(map(int,input().split()))


c = 0
for i in n:
    if d[i]%m==o:
        c += 1    

if c != 0:
    f[1] = 1
    f[2] = 1
    for i in range(c ,m+1) :


