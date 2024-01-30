# This is my zigzag converter 
# The task is to convert the string "PAYPALISHIRING" into a zigzag for a given number of rows - 4 in the example below
# This is the read row by row - "PINALSIGYAHRPI" in example below
'''
P     I    N
A   L S  I G
Y A   H R
P     I
'''

# Leetcode input - not part of actual code
s = "PAYPALISHIRING"
numRow = 4 

# My code 

# Checks that rows entered is not equal to 1 (if 1 then there is no need to compute)
if numRow != 1:
  rows = []

  # Makes list of rows
  for _ in range(numRow):
    rows.append([])

  # Point at which zigzag goes back down (P, I in above example)
  centre = numRow - 1

  # Algorithm to assign the letter to its appropriate row
  for index in range(len(s)): 
    ind = index%(2*numRow - 2)
    LtA = centre - abs(centre - ind) 
    rows[LtA].append(s[index])  

  # Turning list back into string
  newStr = ''
  for list in rows:
    for letter in list:
      newStr += letter 
  
  print(newStr)

else: 
  print(s)
    
  
