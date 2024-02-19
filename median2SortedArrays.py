# This is my solution to the "Median of 2 sorted arrays" problem

nums1 = [1,3]
nums2 = [2]

def findMed(nums1, nums2):
  full_list = sorted(nums1 + nums2)
  
  medInd = ((len(full_list)+1)/2)-1  
  
  if medInd.is_integer(): 
    median = full_list[int(medInd)]
    return median

  else: 
    medInd = int(medInd) 
    median = (full_list[medInd] + full_list[medInd+1])/2
    return median

print(findMed(nums1, nums2))
