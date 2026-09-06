class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = {}
        word2 = {}
        
        if len(s) != len(t):
            return False
        
        for char in s:
            if char in word1:
                word1[char] += 1
            else:
                word1[char] = 1

        for char in t:
            if char in word2:
                word2[char] += 1
            else:
                word2[char] = 1
            
        if word1 == word2:
            return True
        else: 
            return False
            

        


        
