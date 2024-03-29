# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

# hints: Try a hash table
#       Could a bit vector be useful?   (bit vector is a vector of bits)
#       Can you solve it in O(N log N) time? What might a solution like that look like?

# test cases:

# "abcdef" -> True
# "aabxxd" -> False

import string as string_lib

# Implementation with dictionaries
def is_unique(string: str) -> bool:
    
    string = string.replace(" ","").lower() # we prevent edge cases with this

    dictionary = dict()

    for char in string: # O(N) 
        if char in dictionary.keys():
            return False
        else:
            dictionary[char] = 1
        
    return True

# Implementation with no additional data structure
def is_unique_v2(string: str) -> bool:

    string = string.replace(" ","").lower()

    alphabet = string_lib.printable

    for character in string: # O(N) 
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
            
        print("testing",function.__name__+":")

        for text,result in test_cases:
            assert function(text) == result
            # print(function(text) == result)

        print("All test passed\n")