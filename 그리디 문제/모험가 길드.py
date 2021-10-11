n = int(input())
array = list(map(int, input().split()))
count = 0
if n %max(array) != 0:
    count += n//max(array) + 1

else : 
    count += n//max(array)

print(count)