class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        create two variable to point at the front and the back of the list. then using the pointers, add together the two values and compare it to the target. if the sum is larger than the target then we will subtract 1 from the end, else we would add 1 to the beginning. once the target has been reached, add one tothe front and back values and then add them to an empty list and return that
        """

        front = 0
        back = len(numbers) - 1

        sum = numbers[front] + numbers[back]

        if sum == target:
            return [front + 1, back + 1]
        
        while sum != target:
            if sum > target:
                back -= 1

                sum = numbers[front] + numbers[back]
            else:
                front += 1

                sum = numbers[front] + numbers[back]

        return [front + 1, back + 1]
        