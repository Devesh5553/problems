class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] # python doesnt have maxHeap so use minHeap by cinverting all numbers to negative
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0) #if stones doesnt have any element left then add 0
        return abs(stones[0]) #return the abs value of the negative number