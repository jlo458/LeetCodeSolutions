# My solution to the "Longest Palindromic Substring" task

class Solution:
    def longestPalindrome(self, s: str) -> str:

        def findCh(s, ch):
            return [i for i, ltr in enumerate(s) if ltr == ch]

        pals = []
        for _ in range(len(s)-1):
            if s == s[::-1]: 
                pals.append(s)

            else:

                let1 = s[0]
                inds = findCh(s, let1)
                inds.pop(0)
                #print(inds)
            
                for lastLetInd in inds[::-1]: 
                    test = s[:lastLetInd+1]
                    if test == test[::-1]: 
                        pals.append(test)
                        break 
            
                s = s[1:]

        if pals == []:
            return s[0] 

        minLength = 0
        longPal = ''
        for pal in pals: 
            if len(pal) > minLength: 
                minLength = len(pal)
                longPal = pal 

        return longPal
        
