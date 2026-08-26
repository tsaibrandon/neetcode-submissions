class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        create a dict for nums
        create an output array

        for i in range(len(nums))
            second_num = target - nums[i]

            if second_num in seen
                add the index into the output array
                add the second_num index into output array

            if the value at the index is not in the dict
                add the value and then hold its index
        
        return output array
        """

        seen = {}
        output = []

        for i in range(len(nums)):
            second_num = target - nums[i]

            if second_num in seen:
                output.append(seen[second_num])
                output.append(i)

            if nums[i] not in seen:
                seen[nums[i]] = i

        return output