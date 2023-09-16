class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # initialize string
        common_prefix = ""
        shortest_word = min(len(s) for s in strs)
        
        for i in range(shortest_word):
            char = strs[0][i]
            
            # check if char is in the same in all words
            if all(s[i] == char for s in strs):
                common_prefix += char  
            else:
                break
        return common_prefix
    
    
s = Solution()
test = s.longestCommonPrefix(strs = ["flower","flow","flight"])
print(test)