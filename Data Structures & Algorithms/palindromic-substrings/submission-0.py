class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        result = 0

        loop through s using i:
            set left and right pointer to i

            while the pointers are within the string and the values ==:
                move left pointer 1 to the left
                move right pointer 1 to the right

                add 1 to the result
            
            set left and right pointer to i, i + 1

            while the pointers are within the string and the values ==:
                move left pointer 1 to the left
                move right pointer 1 to the right

                add 1 to the result
            
        return result
        """

        result = 0 

        for i in range(len(s)):
            left, right = i, i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

                result += 1
            
            left, right = i, i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

                result += 1
            
        return result