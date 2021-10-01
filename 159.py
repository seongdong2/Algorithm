array = [7, 5, 9, 0, 4, 1, 6, 2, 4, 8]
array.sort()
print(array)

for i in range(len(array)) :
    n = i
    for j in range(i+1, len(array)):
        if array[n] > array[j] :
            n = j

    array[i], array[n] = array[n], array[i]

print(array)        