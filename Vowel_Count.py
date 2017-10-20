def getCount(inputStr):
    num_vowels = 0
    # your code here
    vowels = ["a", "e", "o", "u", "i"]
    for i in inputStr:
        if (i in vowels):
            num_vowels += 1
    return num_vowels
