class Solution:

    #Time Complexity: O(n2)
    def bruteForce(self, nums: List[int], target: int) -> List[int]:

        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]
    

    def optimisedApproach(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range (len(nums)):
            number = nums[i]
            complement = target - number
            if complement in seen:
                return [seen[complement],i]
            seen[number] = i

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #return self.bruteForce(nums, target)

        return self.optimisedApproach(nums, target)
        