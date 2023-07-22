# Given two strings, write a method to decide if one is a permutation of the
# other.

# hints: Try a hash table
#       Could a bit vector be useful?   (bit vector is a vector of bits)
#       Can you solve it in O(N log N) time? What might a solution like that look like?


def check_permutation(string_1: str, string_2: str) -> bool:
    """
    sorted function is N*log(N)    
    """
    # string_1 = string_1.replace(" ","").lower() # O(N)
    # string_2 = string_2.replace(" ","").lower()

    if len(string_1) != len(string_2):
        return False

    return sorted(string_1) == sorted(string_2) # sorted returns a sorted list of elements, ordered by ascii number

def check_permutation_2(string_1: str, string_2: str) -> bool:
    """
    complexity O(N)     
    """
    # string_1 = string_1.replace(" ","").lower() # O(N)
    # string_2 = string_2.replace(" ","").lower()

    if len(string_1) != len(string_2):
        return False

    char_counter = dict()

    for character in string_1: # O(N)

        if character in char_counter.keys(): # O(1) in avg case, O(N) worst case (https://wiki.python.org/moin/TimeComplexity)
            char_counter[character] += 1
        else:
            char_counter[character] = 1

    for character in string_2: # O(N)

        if character in char_counter.keys():
            char_counter[character] -= 1
        else:
            char_counter[character] = 1

    if list(char_counter.values()).count(0) == len(char_counter): # O(N)
        return True
    else:
        return False

if __name__ == "__main__":

    functions = [
                check_permutation,
                check_permutation_2
                ]
        
    test_cases = [
                    ("dog", "god", True),
                    ("abcd", "bacd", True),
                    ("3563476", "7334566", True),
                    ("wef34f", "wffe34", True),
                    ("dogx", "godz", False),
                    ("abcd", "d2cba", False),
                    ("2354", "1234", False),
                    ("dcw4f", "dcw5f", False),
                    ("DOG", "dog", False),
                    ("dog ", "dog", False),
                    ("aaab", "bbba", False)
                    ]

    for function in functions:
    
        print("\ntesting",function.__name__+":")

        for text1, text2, expected in test_cases:
            assert function(text1, text2) == expected

        print("All tests passed for",function.__name__+"")

    print("\nAll tests passed\n")