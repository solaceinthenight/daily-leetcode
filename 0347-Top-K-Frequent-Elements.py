from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        feq_table = Counter(nums)
        pq = []
        for num, feq in feq_table.items():
            heapq.heappush(pq, (-feq, num))
        return [heapq.heappop(pq)[1] for i in range(k)]
