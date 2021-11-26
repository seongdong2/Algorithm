import heapq
def solution(scoville, K):
    answer = 0
    if can_Check(scoville, k): return -1
    
    while 
    
    
    
    return answer


def mount(iterable):
    mix_array = heapsort(interable)
    return mix_array[0] + (mix_array[1]*2)

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


def can_Check(iterable, k): 
    return True if k > reduce(lambda x, y: x + y, iterable) else False