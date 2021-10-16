n, m = map(int, input().split())
p= list(map(int, input().split()))

array = [0] * 11

for x in p :
    array[x] += 1

rst = 0
for i in range(1, m+1):
    n -= array[i]
    rst += array[i]*n

print(rst)



