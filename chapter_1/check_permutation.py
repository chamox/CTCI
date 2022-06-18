# Given two strings, write a method to decide if one is a permutation of the
# other.

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

        if character in char_counter.keys():
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

    
        print("testing",function.__name__,":")

        for text1, text2, expected in test_cases:
            # print(text1, text2, expected)
            # print()

            print(function(text1, text2) == expected)
            assert function(text1, text2) == expected

        print("\n")