# My solution to "Lemonade Change" problem 

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        def remove(change, num): 
            try: 
                change.remove(num)
                return change

            except: 
                return 'False'

        
        change = []
        for bill in bills: 
            owed = bill - 5
            if owed == 5:
                change = remove(change, 5)
                if change == 'False': 
                    return False
            

            elif owed == 15: 
                change1 = remove(change, 10)
                if change1 == 'False': 
                    for _ in range(3): 
                        change = remove(change, 5)

                    if change == 'False': 
                        return False
                    continue

                change = change1
                change = remove(change, 5)
                if change == 'False': 
                    return False

            change.append(bill)
            

        return True
        
