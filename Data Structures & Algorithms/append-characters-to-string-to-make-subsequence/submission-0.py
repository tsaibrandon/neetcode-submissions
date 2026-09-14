class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """
        first, second pointer = 0

        while both pointers are in range of str len:
            if both values ==:
                add one to the second pointer
            
            add 1 to the first pointer
        
        return len(t) - (second)
        """

        first = second = 0

        while first < len(s) and second < len(t):
            if s[first] == t[second]:
                second += 1
            
            first += 1
        
        return len(t) - second