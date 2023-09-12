class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        number = str(x)
        length = len(number)
        
        for i in range(length // 2):
            if number[i] != number[length-1-i]:
                return False
            
        return True

test = Solution()
ress = test.isPalindrome(1221)
print(ress)