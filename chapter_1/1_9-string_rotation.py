# String Rotation:Assumeyou have a method isSubstringwhich checks if one word is a substring
# of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
# call to isSubstring(e.g.,"waterbottle"is a rotation of"erbottlewat")


def rotateString(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    return goal in s+s