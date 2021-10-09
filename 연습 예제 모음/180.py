n = int(input())

array = []
for i in range(n) :
    array.append(input().split())

def setting(data) :
    return data[1]

result = sorted(array, key=setting)

print(result)

for i in result :
        print(i[0], end=' ')