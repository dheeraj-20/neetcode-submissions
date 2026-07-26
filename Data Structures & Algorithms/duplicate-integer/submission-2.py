class Solution:

    def findDuplicateBruteForce(self, nums: List[int]) -> bool:

        for i in range (0, len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i] == nums[j]):
                    return True
        
        return False
    
    def findDuplicateOptimised(self, nums: List[int]) -> bool:
        dictNums = {}
        for i in range(len(nums)):
            dictNums[nums[i]] = dictNums.get(nums[i], 0) + 1
            if dictNums[nums[i]]>1:
                return True
        return False

    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #Brute Force Approach
        #return self.findDuplicateBruteForce(nums)

        #Optimised Approach
        return self.findDuplicateOptimised(nums)

    
    