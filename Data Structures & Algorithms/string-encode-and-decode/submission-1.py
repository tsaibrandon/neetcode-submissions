class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        create an empty list called code

        for each word in the list of strings:
            append the length of the word + "#" and then the word
        """

        code =[]

        for word in strs:
            code.append(str(len(word)) + "#" + word)

        return "".join(code) 
        
    def decode(self, s: str) -> List[str]:
        """
        create an empty list called result
        create a pointer i, starting at 0

        while i is less than len(s):
            find the index of the next "#" starting search from i, call it hashIndex
            get the substring from i to hashIndex, convert it to an int -> this is length
            
            the word starts right after hashIndex (hashIndex + 1)
            the word ends at (hashIndex + 1 + length)
            grab that substring -> this is the word

            append the word to result

        return result
        """
        
        result = []
        i = 0

        while i < len(s):
            hashIndex = s.find("#", i)
            length = int(s[i:hashIndex])
            
            start = hashIndex + 1
            end = start + length
            
            word = s[start:end]
            result.append(word)
            
            i = end

        return result

