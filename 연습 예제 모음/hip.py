import heapq
def heapsort(iterable):
    h= []
    result = []

    for value in iterable :
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

#실행결과 [0,1,2,3,4,5,6,7,8,9]