class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lengthOfArray = len(nums)
        ans = []
        for i in range(0, 2*lengthOfArray):
            ans.append(nums[i % lengthOfArray])
        
        return ans
        