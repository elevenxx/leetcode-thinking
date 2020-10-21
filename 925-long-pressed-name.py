class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
    
        # two pointers tech
        # elements in typed, fit with elements in name under two kinds of situations
        # first, name[i] == typed[j]
        # second, typed[j] == typed[j-1]
        # others are not desirable, so return False
        
        i, j = 0, 0
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j-1]:
                j += 1
            else:
                return False
        
        # when j traverse to the end of typed, 
        # see if i also traverse to the end of name
        return i == len(name)
