class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create a dictionary for s
        #create a dictionary for t

        #if the length of s == the length of t
            #for the length of s
                #if the letter has been seen in the dict
                    #increase the count for that letter
                #else
                    # add the letter into the dict setting the count to 1
                
                #do the same for t
            
            #if dict s == dict t
                #reutrn true
            #else
                #return false
        #else
            #return false

        s_count = {}
        t_count = {}

        if len(s) == len(t):
            for char in s:
                if char in s_count:
                    s_count[char] += 1
                else:
                    s_count[char] = 1
            
            for char in t:
                if char in t_count:
                    t_count[char] += 1
                else:
                    t_count[char] = 1

            if s_count == t_count:
                return True
            else:
                return False
        else:
            return False
            
            