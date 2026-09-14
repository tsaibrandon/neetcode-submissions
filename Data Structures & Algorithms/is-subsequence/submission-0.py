class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        first pointer = 0
        second pointer = 0

        while the first pointer has not reached the end of s:
            if and first < len(s) and second < len(t) and s[first] == t[second]:
                add 1 to first pointer
                add 1 to second pointer
            elif first < len(s) and second < len(t) and s[first] != t[second]:
                add 1 to the second pointer
            else:
                return false

        return true
        """

        first, second = 0, 0

        while first < len(s):
            if first < len(s) and second < len(t) and s[first] == t[second]:
                first += 1
                second += 1
            elif first < len(s) and second < len(t) and s[first] != t[second]:
                second += 1
            else:
                return False
        
        return True