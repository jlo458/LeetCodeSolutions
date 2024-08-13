# My code for "Reverse Integer" leetcode challenge

class Solution:
    def reverse(self, num: int) -> int:
        negative = False
        if num < 0: 
            negative = True
            num = abs(num)

        num = str(num)
        num = num[::-1]
        num = int(num)

        if negative: 
            num = 0-num
            if num < -(2**31): 
                return 0 

        else: 
            if num > (2**31)-1: 
                return 0 

        return num 
