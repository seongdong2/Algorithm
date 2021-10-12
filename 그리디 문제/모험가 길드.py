n = int(input())
array = list(map(int, input().split()))
array.sort()


count = result = 0
for i in array :
    result +=1
    if result == i :
        count += 1
        result = 0

    

print(count)