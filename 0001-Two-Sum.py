class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in store:
                return list((i, store[comp]))
            else:
                store[num] = i
