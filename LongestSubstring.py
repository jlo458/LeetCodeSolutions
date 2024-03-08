# This is my solution to the leetcode "Longest Substring Without Repeating Characters" problem

def length_of_longest_substring(s):
  longest_sub = []
  current_sub = []

  for letter in s:
      if letter in current_sub:
          current_sub = current_sub[current_sub.index(letter) + 1:]

      current_sub.append(letter)

      if len(current_sub) > len(longest_sub):
          longest_sub = current_sub[:]

  return len(longest_sub)

the_string = "abcacbb" 
print(length_of_longest_substring(the_string))
