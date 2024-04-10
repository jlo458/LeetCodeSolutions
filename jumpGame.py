# This is my solution to Leetcode "Jump Game" problem 
# Initially, I tried to solve it recursively but found that it exceeded the time limit
# So instead, found that dynamic programming worked a lot better


class Solution:
    def can_Jump(self, nums: List[int]) -> bool:
        max_reachable = 0
        final_index = len(nums) - 1
        
        for i, num in enumerate(nums):
            if i > max_reachable:
                return False  # If we can't reach this index, return False
            max_reachable = max(max_reachable, i + num)
            if max_reachable >= final_index:
                return True  # If we can reach or go beyond the final index, return True
        
        return False
