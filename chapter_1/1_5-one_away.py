# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

# insert, remove, replace

from textwrap import shorten


def one_way(string_1: str, string_2: str) -> bool:

    # first case: same length -> replace.
    if len(string_1) == len(string_2):
        if string_1 == string_2:
            return True
        changes = 0
        for i in range(len(string_2)):
            if string_1[i] != string_2[i]:
                changes += 1
                if changes > 1:
                    return False
        if changes == 1:
            return True
    

    # second case: different length (insert or remove)    

    if abs(len(string_1) - len(string_2)) == 1:
        # I need to get the short and the large string
        if len(string_1) > len(string_2):
            short = string_2
            large = string_1
        else:
            short = string_1
            large = string_2

        i = 0
        changes = 0

        while i < len(short): # 3

            if large[i+changes] == short[i]:
                i+=1

            else:
                changes += 1

                if changes > 1: 
                    return False
                    
        return True    

    else:
        return False


if __name__ == "__main__":

    test_cases = [
        # no changes
        ("pale", "pale", True),
        ("", "", True),
        # one insert
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pales", "pale", True),
        ("ples", "pales", True),
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        # one replace
        ("pale", "bale", True),
        ("a", "b", True),
        ("pale", "ble", False),
        # multiple replace
        ("pale", "bake", False),
        # insert and replace
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
        # permutation with insert shouldn't match
        ("ale", "elas", False),
    ]

    functions = [
                one_way     
                ]

    for function in functions:
    
        print("testing",function.__name__,":")

        for text1, text2, expected in test_cases:

            print(function(text1,text2) == expected)
            assert function(text1,text2) == expected

        print("\n")