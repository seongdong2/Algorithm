array = [7, 5, 9, 0, 4, 1, 6, 2, 4, 8]

def quick(array, start, end):
    if start >= end :
        return
    p = start
    left = start+1
    right = end
    while left <= right :
        while left <= end and array[left] <= array[p] :
            left += 1
        while right >= start and array[right] >= array[start]:
            right -= 1
        if left > right :
            array[right], array[p] = array[right], array[p]
    else :
        array[left], array[right] = array[right], array[left]

    quick(array, start, right-1)
    quick(array, right+1 , end)

quick(array, 0, len(array)-1 )
print(array)
