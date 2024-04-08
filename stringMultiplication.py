# This is my solution to "Multiply Strings" problem on Leetcode 

num1 = "123"
num2 = "456"
numSum = []

for ind1 in range(len(num1)):
  for ind2 in range(len(num2)): 
    #pow1 = ind1 + 1
    #pow2 = ind2 + 1

    total = int(num1[len(num1)-ind1-1]) * int(num2[len(num2)-ind2-1])
    total = total * 10**(ind1+ind2)

    numSum.append(total)


print(sum(numSum))
