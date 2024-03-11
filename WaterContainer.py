# My solution to "Container With Most Water" Leetcode problem

class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftInd = 0
        rightInd = len(height) - 1
        maxArea = 0

        while left < right:
            currentArea = min(height[leftInd], height[rightInd]) * (rightInd - leftInd)
            maxArea = max(maxArea, currentArea)

            if height[leftInd] < height[rightInd]:
                leftInd += 1
            else:
                rightInd -= 1

        return maxArea

  
