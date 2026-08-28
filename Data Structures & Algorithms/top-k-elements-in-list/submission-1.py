class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        create an empty dict called counts
        create an empty list called output

        for each number in nums:
            if it has been seen in counts:
                increase the value by one
            else:
                add the number to the dict and set its value to 1
        
        create the buckets with (len(nums) + 1)

        for every pair in the dict:
            add the number into the bucket of the index matching the frequency
        
        for every frequency in the bucket down to 1:
            for every number in the bucket 
                add the number into the output list
                
                if the output list length == k:
                    return output
            
        return output
        """

        counts = {}
        output = []

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for key,value in counts.items():
            buckets[value].append(key)
        
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                    output.append(num)

            if len(output) == k:
                return output
        
        return output



