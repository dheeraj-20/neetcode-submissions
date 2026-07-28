class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
            
        nums.sort()
        maxResult = 1
        currentCount = 1
        for i in range(1, len(nums)):
            if(nums[i] == nums[i-1]+1):
                currentCount += 1
            elif(nums[i] == nums[i-1]):
                continue
            else:
                maxResult = max(currentCount, maxResult)
                currentCount = 1

        return max(maxResult, currentCount)
