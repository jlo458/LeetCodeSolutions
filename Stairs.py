# This is my solution to the "Climbing Stairs" Leetcode problem

n = 6

def stairs(n):
  n1 = 1 
  n2 = 1 

  sum = 1
  
  if n > 1:
    for _ in range(n-1): 
      sum = n1 + n2
      n1 = n2 
      n2 = sum 

  return sum


print(stairs(n))
