# This is my solution to "Two Sum" Leetcode problem

nums = [-3,4,3,90]
target = 0


def findSum(nums, target):
  theNums = nums.copy()
  for _ in range(len(theNums)):
    firstNum = theNums[0]
    theNums.pop(theNums.index(firstNum))      
    for num in theNums: 
       sum = firstNum + num  
       if sum == target:
         #print(nums)

         ans1 = nums.index(firstNum)
         #nums.pop(nums.index(firstNum))
         nums[nums.index(firstNum)] = '_'
         ans2 = nums.index(num)
         answer = [ans1, ans2]
         return answer

  return None


print(findSum(nums, target))
