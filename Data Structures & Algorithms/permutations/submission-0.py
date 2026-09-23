class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False
        """
        res = []
        sub = []

        used = [False] * len(nums)

        def dfs():
            if len(sub) == len(nums):
                res.append(sub.copy())
                return
            
            for j in range(len(nums)):
                if used[j]:
                    continue
                
                used[j] = True
                sub.append(nums[j])
                dfs()
                sub.pop()
                used[j] = False

        dfs()
        return res