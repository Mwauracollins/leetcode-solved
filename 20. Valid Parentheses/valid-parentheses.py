class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        bracket_map = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        for char in s:
            # if current bracket is opening add to stack
            if char in bracket_map.values():
                stack.append(char)
            #     if current bracket is closing,,,
            elif char in bracket_map.keys():
                # check if there is empty. if Not pop the top element in stack and check k-v matches
                if not stack or stack.pop() != bracket_map[char]:
                    return False
            else:
                return False

        return not stack

s = Solution()
test = s.isValid('({}[{}])')
print(test)
