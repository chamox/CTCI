# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

# test cases:

# "abcdef" -> True
# "aabxxd" -> False


def is_unique(string: str) -> bool:
    
    dictionary = dict()

    for char in string:
        if char in dictionary.keys():
            return False
        else:
            dictionary[char] = 1
        
    return True

if __name__ == "__main__":
    
    test_cases = [
                  ("abcdef", True),
                  ("aabxxd", False),
                  ("",True)
                 ]

    for text,result in test_cases:
        print(is_unique(text) == result)