# In progress 

arrays = [[1,5],[3,4]]

def maxDistance(arrays): 
  if len(arrays) == 0: 
    return 0
  smallest = arrays[0][-1] + 1
  #highest = arrays[0][0]

  sList = None 
  s2List = None
  #hList = None

  for ind in range(len(arrays)): 
    if arrays[ind][0] < smallest:
      s2List = sList
      smallest = arrays[ind][0]
      sList = ind 

  highest = arrays[0][0] - 1
  hList = None
  h2List = None

  for ind in range(len(arrays)): 
    if arrays[ind][-1] > highest:
      h2List = hList
      highest = arrays[ind][-1]
      hList = ind

  if hList == sList: 
    try:
      opt1 = highest - arrays[s2List][0]
      opt2 = arrays[h2List][-1] - smallest 
      if opt1 > opt2: 
        smallest = arrays[s2List][0]

      else: 
        highest = arrays[h2List][-1]

    except: 
      return maxDistance(arrays.pop(hList)) 

  return highest - smallest

print(maxDistance(arrays))
