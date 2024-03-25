# This is my solution for the "Find all duplicates in an array" problem on leetcode 
# This isn't as easy as it seems because a knowledge of sets (and hash tables) is required

nums = [13,8,5,3,20,12,3,20,5,16,9,19,12,11,13,19,11,1,10,2]

inNums = set()
dups = set()

for num in nums:
    if num in inNums:
        dups.add(num)
    else:
        inNums.add(num)

print(list(dups))

