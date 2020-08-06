def no_dups(s):
    # Your code here
    table = {}

    # loop over every word in string, and add each word to a table as a key
    for word in s.split():
        if not word in table:
            table[word] = 1

    # map over keys in table, append each to returnString as well as a whitespace
    returnString = ''
    for x in table:
        returnString += x
        returnString += ' '

    # remove last element from returnString as it has an extra whitespace
    return returnString[:-1]


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
