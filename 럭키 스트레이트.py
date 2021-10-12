#import sys
#input = sys.stdin.readline
n = list(map(int, input()))
rst_l = rst_r = 0

mid = len(n)//2
for i in range(mid):
    rst_r += n[i]

for j in range(mid, len(n)):
    rst_l += n[j]

print(rst_l)
print(rst_r)


if rst_l == rst_r :
    print('LUCKY')
else : 
    print('READY')
