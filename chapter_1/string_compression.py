# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def string_compression(string: str) -> str:
    
    #iterate over the string and count the actual quantity of the letter

    if string == "":
        return ""

    i=0
    counter = 1
    compressed = ""

    while i < (len(string) - 1): # finish before the last element

        if string[i] == string[i+1]:
            counter+=1
        else:
            compressed+= string[i] + str(counter)
            counter = 1
        i+=1

    compressed+= string[i] + str(counter)

    if len(compressed)>=len(string):
        return string    
    
    return compressed

        
if __name__ == "__main__":

    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),

    ]
    functions = [
        string_compression,
    ]

    for function in functions:
        
            print("testing",function.__name__,":")

            for text1,expected in test_cases:

                print(function(text1) == expected)
                assert function(text1) == expected

            print("\n")