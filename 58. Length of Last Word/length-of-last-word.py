class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()

        if not words:
            return 0

        return len(words[-1])

s = Solution()
test = s.lengthOfLastWord("   fly me   to   the moon  ")
print(test)


