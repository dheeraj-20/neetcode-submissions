class Solution:

    def bruteForce(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            
        sArray = [0] * 26

        for char in s:
            sArray[ord(char) - ord('a')]+=1
        
        for char in t:
            sArray[ord(char) - ord('a')]-=1
 
        for i in range(0, len(sArray)):
            if sArray[i] != 0:
                return False

        return True

    def isAnagram(self, s: str, t: str) -> bool:
        
        #Space Complexity: O(26) = O(1), Time Complexity O(s + t)
        return self.bruteForce(s, t)