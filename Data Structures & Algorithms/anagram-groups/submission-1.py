class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        create an empty dict
        create an empty list

        for every word in the list:
            sort the word and turn it back into a str

            if the sorted word is in the dict:
                add the word into the list/value
            else:
                add the the sorted word as the key with a value of the word
            
        for every key in the dict:
            add the list of words into the empty list as a list
        
        return the list
        """

        groups = {}
        sort = []
        output = []

        for i in range(len(strs)):
            sort.append("".join(sorted(strs[i])))

            if sort[i] in groups:
                groups[sort[i]].append(strs[i])
            else:
                groups[sort[i]] = [strs[i]]
            
        for lists in groups.values():
            output.append(lists)

        return output