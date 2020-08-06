def word_count(s):
    # Your code here
    dictionary = {}

    ignoreCharacters = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'

    for char in ignoreCharacters:
        s = s.replace(char, ' ')

    print(s)

    for word in s.split():

        # if word exists in dictionary as a key already, increase count by 1
        if word.lower() in dictionary:
            dictionary[word.lower()] += 1
        # if word is not yet in the dictionary, add it and set count to 1
        else:
            dictionary[word.lower()] = 1

    return dictionary


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
