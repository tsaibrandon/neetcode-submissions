class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        create a res list
        create a subset list

        sort candidates list

        def dfs(i, target):
            if the i >= len(candidates) or target < 0:
                return 
            if target == 0:
                append a copy of subset to res
                return
            
            append nums[i] to subset
            subtract nums[i] from target
            dfs(i+1, target)

            pop the subset
            add nums[i] to target
            
            while nums[i+1] == nums[]:
                i += 1
            dfs(i, target)
        
        dfs(0, target)
        return result
        """

        res = []
        subset = []

        candidates.sort()

        def dfs(i, target):
            if target == 0:
                res.append(subset.copy())
                return
            if i >= len(candidates) or target < 0:
                return
            
            subset.append(candidates[i])
            dfs(i+1, target - candidates[i])

            subset.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            dfs(i+1, target)
        
        dfs(0, target)
        return res