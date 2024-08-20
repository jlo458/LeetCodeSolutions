# My solution to "Maximum Distance in Arrays" problem on Leetcode

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        if len(arrays) == 0:
            return 0
    
        min_val = float('inf')
        second_min_val = float('inf')
        max_val = float('-inf')
        second_max_val = float('-inf')
        min_idx = -1
        max_idx = -1
        
        for i, array in enumerate(arrays):
            if array[0] < min_val:
                second_min_val = min_val
                min_val = array[0]
                min_idx = i
            elif array[0] < second_min_val:
                second_min_val = array[0]
            
            if array[-1] > max_val:
                second_max_val = max_val
                max_val = array[-1]
                max_idx = i
            elif array[-1] > second_max_val:
                second_max_val = array[-1]
        
        if min_idx != max_idx:
            return max_val - min_val
        else:
            return max(second_max_val - min_val, max_val - second_min_val)
        
