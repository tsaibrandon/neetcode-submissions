class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen = {}

        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
                
        output = []

        for i in range(1, len(nums)+1):
            if i not in seen:
                output.append(i)

        return output

                
