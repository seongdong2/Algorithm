n = int(input())

array = []
for i in range(n) :
    id = input().split()
    array.append((id[0], int(id[1])))

#def setting(data) :
#    return data[1]
#result = sorted(array, key=setting)


array = sorted(array, key=lambda result: result[1])

print(array)
for result in array :
        print(result[0], end=' ')