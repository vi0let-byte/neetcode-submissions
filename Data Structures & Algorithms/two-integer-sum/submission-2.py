class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        numPairs = {}
        for i in range(len(nums)):
            numPairs[target - nums[i]] = i
        for key in numPairs.keys():
            if key in nums:
                n1 = nums.index(key)
                n2 = numPairs[key]
                if n2 > n1:
                    return [n1, n2]
                elif n1 > n2:
                    return [n2, n1]            