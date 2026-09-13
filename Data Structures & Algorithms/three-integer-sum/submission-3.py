class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        create an empty results list
        sort nums in ascedning order

        loop i from 0 to len(nums) - 3:
            if i > 0 and if the value of the current i == the value of the previous i:
                skip this i

            set the target = -nums[i]

            set front pointer = i + 1
            set back pointer = len(nums) - 1

            while the front value < back value:
                find the sum of the front and back pointer values

                if the sum == target:
                    add the values for i, front, and back into a list
                    add the list into the results list

                    add 1 to the front value
                    subtract 1 from the back value

                    while the front value == the previous front value:
                        add 1 to the front value

                    while the back value == the previous back value:
                        subtract 1 from the back value
                elif sum > target:
                    subtract 1 from the back value
                else:
                    add 1 to the front value
                
        return the results list
        """

        result = []
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = -nums[i]

            front = i + 1
            back = len(nums) - 1

            while front < back:
                sum = nums[front] + nums[back]

                if sum == target:
                    triplet = [nums[i], nums[front], nums[back]]
                    result.append(triplet)

                    front += 1
                    back -= 1

                    while front < back and nums[front] == nums[front-1]:
                        front += 1
                    
                    while front < back and nums[back] == nums[back+1]:
                        back -= 1
                elif sum > target:
                    back -= 1
                elif sum < target:
                    front += 1
        
        return result