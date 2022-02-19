import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
#[0,1,2,3,4,5,6,7,8,9]

# 최대힙으로 만들고자 한다면 value를 -value로 넣었다가 -로 빼준다.
