class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        the idea is to have a variable point at the front of the str and then have another point at the 
        end. then check if each variable == at each iteration. we have to first remove any non-
        alphanumeric characters and make everything the same case. 
        """

        lower = s.lower()
        clean = "".join(c for c in lower if c.isalnum())
        
        i = 0
        end = len(clean) - 1

        while i < end:
            if clean[i] != clean[end]:
                return False

            i += 1
            end -= 1
        
        return True
            
            


                