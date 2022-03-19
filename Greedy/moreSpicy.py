import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while len(scoville) > 1:
        food1 = heapq.heappop(scoville)
        food2 = heapq.heappop(scoville)
        if food1 >= K:
            return count
        mixedFood = food1 + food2 * 2
        count += 1
        heapq.heappush(scoville, mixedFood)
    
    if count == 1:
        return count
    
    return -1


        
solution([1, 2, 3, 9, 10, 12], 7)
        
            
        
        
 
