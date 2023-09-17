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
            if number[i] != number[length - 1 - i]:
                return False

        return True


s = Solution()
test = s.isPalindrome(121921)
print(test)
