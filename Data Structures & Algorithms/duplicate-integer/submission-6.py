class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        seen = set()

        loop through nums:
            add value to set if havent seen
            if seen return false
        
        return true
        """

        seen = set()

        for n in nums:
            if n not in seen:
                seen.add(n)
            else:
                return True

        return False