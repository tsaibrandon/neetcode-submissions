class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        res = []
        subset = []

        def dfs(i, target):
            if i >= len(nums) or target < 0:
                return
            if target == 0:
                append copy of subset to result
                return
            
            subset.append(nums[i])
            target -= nums[i]
            dfs(i, target)

            subset.pop()
            target += nums[i]
            dfs(i + 1, target)
        
        dfs(0, target)
        return res
        """

        res = []
        subset = []

        def dfs(i, target):
            if i >= len(nums) or target < 0:
                return
            if target == 0:
                res.append(subset.copy())
                return

            subset.append(nums[i])
            target -= nums[i]
            dfs(i, target)

            subset.pop()
            target+= nums[i]
            dfs(i+1, target)
        
        dfs(0, target)
        return res