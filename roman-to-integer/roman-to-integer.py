class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        number = 0
        i = 0
        while i < len(s):
            cur_val = map[s[i]]
            if i + 1 < len(s):
                next_val = map[s[i + 1]]
                if cur_val < next_val:
                    number += next_val - cur_val
                    i += 2
                else:
                    number += cur_val
                    i += 1
            else:
                number += cur_val
                i += 1

        return number
