import sys
#input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))

big_num = 0
for i in range(n) :
    big_num += array[i]

print(big_num)



