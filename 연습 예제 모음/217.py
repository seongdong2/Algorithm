x = int(input())
d = [0]*10000

for i in range(2, x+1):
    d[i] = d[i-1]-1
    if d[i]%5==0 :
        d[i] = min(d[i], (d[i]//5)+1)
    if d[i]%2==0 :
        d[i] = min(d[i], (d[i]//2)+1)
    if d[i]%3==0 :
        d[i] = min(d[i], (d[i]//2)+1)

print(d[x])
    
    




    