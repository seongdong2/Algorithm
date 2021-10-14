#import sys
#input = sys.stdin.readline
n = input()
length = len(n)
rst = 0

for i in range(length//2):
    rst += int(n(i))

for j in range(mid, len(n)):
    rst -= int(n[i])


if rst == 0 :
    print('LUCKY')
else : 
    print('READY')
