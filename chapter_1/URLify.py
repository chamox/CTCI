# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith ", 13
# Output: "Mr%20John%20Smith"

def urlify(string: str, lenght: int) -> str:

    return string[:lenght].replace(" ","%20")


if __name__ == "__main__":

    functions = [
                 urlify
                ]
    

    test_cases = [
                    [("much ado about nothing      ", 22), "much%20ado%20about%20nothing"],
                    [("Mr John Smith       ", 13), "Mr%20John%20Smith"],
                    [(" a b    ", 4), "%20a%20b"],
                    [(" a b       ", 5), "%20a%20b%20"],
                ]

    for function in functions:

    
        print("testing",function.__name__,":")

        for i, expected in test_cases:

            print(function(i[0], i[1]) == expected)
            assert function(i[0], i[1]) == expected

        print("\n")