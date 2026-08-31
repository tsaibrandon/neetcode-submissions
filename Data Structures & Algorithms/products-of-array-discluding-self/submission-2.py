class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        create output array of size len(nums), filled with 1s

        # Pass 1: left products
        create runningLeft = 1
        for i from 0 to len(nums)-1:
            output[i] = runningLeft
            runningLeft = runningLeft * nums[i]

        # Pass 2: right products, multiplied directly into output
        create runningRight = 1
        for i from len(nums)-1 down to 0:
            output[i] = output[i] * runningRight
            runningRight = runningRight * nums[i]

        return output
        """

        n = len(nums)
        output = [1] * n

        runningLeft = 1
        for i in range(n):
            output[i] = runningLeft
            runningLeft *= nums[i]

        runningRight = 1
        for i in range(n - 1, -1, -1):
            output[i] *= runningRight
            runningRight *= nums[i]

        return output