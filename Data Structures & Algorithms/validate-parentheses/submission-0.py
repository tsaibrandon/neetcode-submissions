class Solution:
    def isValid(self, s: str) -> bool:
        """
        creat a dict with the valid brackets
        create an empty stack

        loop through the list 
            check to see if the bracket is valid using the dict
            if not then return false
            if yes then keep apending until closing bracket 
                check the closing bracket to see if valid 
                pop the opening bracket 
        
        return true when the stack is empty
        """

        brackets = {")" : "(", "}" : "{", "]" : "["}
        stack = []

        for char in s:
            if char in brackets:
                if len(stack) == 0:
                    return False
                
                if brackets[char] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        
        return len(stack) == 0