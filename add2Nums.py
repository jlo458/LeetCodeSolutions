# This is my solution to the Leetcode "Add 2 numbers" problem 
# I came up with a solution that worked with a normal list below, but needed some help from ChatGPT for it to work with OOP

# Definition for linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        trial = ListNode(0)
        current = trial
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return trial.next


'''
def addTwoNumbers(l1, l2):
  newList = [] 
  carry = 0
  if len(l1) >= len(l2): 
      size = len(l1) 
      smallSize = len(l2)
      bigList = l1 

  else: 
      size = len(l2)  
      smallSize = len(l1)
      bigList = l2

  for i,j in zip(l1, l2):
      unit = i + j + carry 
      carry = 0
      if unit > 9: 
          unit = str(unit)
          unit = int(unit[1])  
          carry = 1  
      newList.append(unit) 

  for i in range(size-smallSize):  
      unit = bigList[i+smallSize] + carry 
      carry = 0 
      if unit > 9: 
          unit = str(unit)
          unit = int(unit[1])  
          carry = 1  

      newList.append(unit) 

  if carry == 1: 
      newList.append(1)

  
  return newList

l1 = [9,9,9,9,9]
l2 = [9,9,9,9]
print(addTwoNumbers(l1, l2))
'''
