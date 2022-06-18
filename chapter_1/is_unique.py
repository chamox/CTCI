# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

# test cases:

# "abcdef" -> True
# "aabxxd" -> False

import string as string_lib

# Implementation with dictionaries
def is_unique(string: str) -> bool:
    
    dictionary = dict()

    for char in string:
        if char in dictionary.keys():
            return False
        else:
            dictionary[char] = 1
        
    return True

# Implementation with no adsitional data structure
def is_unique_v2(string: str) -> bool:

    alphabet = string_lib.printable

    for character in string:
        if character in alphabet:
            alphabet = alphabet.replace(character,"") # we need to reasign this variable.
        else:
            return False

    return True

if __name__ == "__main__":

    functions = [
                 is_unique,
                 is_unique_v2
                ]
    
    test_cases = [
                  ("abcdef", True),
                  ("aabxxd", False),
                  ("DEF",True)
                 ]

    for function in functions:

      
        print("testing",function.__name__,":")

        for text,result in test_cases:
            print(function(text) == result)
 
        print("\n")