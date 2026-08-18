class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        initialWord = strs[0]
        res = ""
        for i in range(0, len(initialWord)):
            for j in range(1, len(strs)):
                if strs[j] == "" or i>len(strs[j])-1 or initialWord[i] != strs[j][i]:
                    return res
            res += initialWord[i]
        
        return res
