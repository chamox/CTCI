# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco cta", etc.)


def palindrome_permutation(string: str) -> bool:

    chars_counter = dict()

    string = string.replace(" ","").lower()

    for c in string:
        if c in chars_counter:
            chars_counter[c] += 1
        else:
            chars_counter[c] = 1

    odds = 0

    for key in chars_counter:
        if chars_counter[key] % 2 != 0 and odds == 0:
            odds += 1
        elif chars_counter[key] % 2 != 0 and odds != 0:
            return False
    return True






if __name__ == "__main__":
    
    palindrome_permutation("aafggf")

    test_cases = [
                    ("aba", True),
                    ("aab", True),
                    ("abba", True),
                    ("aabb", True),
                    ("a-bba", True),
                    ("a-bba!", False),
                    ("Tact Coa", True),
                    ("jhsabckuj ahjsbckj", True),
                    ("Able was I ere I saw Elba", True),
                    ("So patient a nurse to nurse a patient so", False),
                    ("Random Words", False),
                    ("Not a Palindrome", False),
                    ("no x in nixon", True),
                    ("azAZ", True),
                ]

    functions = [
                palindrome_permutation     
                ]


    for function in functions:
    
        print("testing",function.__name__,":")

        for text,expected in test_cases:

            print(function(text) == expected)
            assert function(text) == expected

        print("\n")