class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        create a result list
        create a subset list

        def dfs(i):
            if i >= length of nums:
                append a copy of subset to the result list
                return

            append nums[i] to subset list
            dfs(i + 1)

            pop from subset list
            dfs(i + 1)
        
        dfs(0)
        return result
        """

        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res