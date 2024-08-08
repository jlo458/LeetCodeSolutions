# In progress

string = "babad"

def findCh(string, ch):
  return [i for i, ltr in enumerate(string) if ltr == ch]

def findPal(string):
  for _ in range(len(string)):
    if string == string[::-1]: 
      return string

    let1 = string[0]
    inds = findCh(string, let1)
    inds.pop(0)
    #print(inds)

    for _ in range(len(inds)): 
      lastLetInd = inds[-1]
      if string[:lastLetInd-1] == string[:lastLetInd-1][::-1]: 
        
    

findPal(string)
  
