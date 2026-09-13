class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        set a max area variable = 0
        
        front pointer would = 0
        back pointer would be len(heights) - 1

        while front < back:
            length = the shorter height between the two pointers
            width = back - front

            area = length * width

            if the area > max area:
                set the max area = area
            
            if heights[front] < heights[back]:
                front += 1
            else:
                back -= 1
        
        return the max area
        """

        max_area = 0

        front = 0
        back = len(heights) - 1

        while front < back:
            length = min(heights[front], heights[back])
            width = back - front

            area = length * width

            if area > max_area:
                max_area = area

            if heights[front] < heights[back]:
                front += 1
            else:
                back -= 1
        
        return max_area