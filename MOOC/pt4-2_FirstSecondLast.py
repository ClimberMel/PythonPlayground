''' Please write three functions: first_word, second_word and last_word. Each function takes a string argument.

As their names imply, the functions return either the first, the second or the last word in the sentence they receive as their string argument.

In each case you may assume the argument string contains at least two separate words, and all words are separated by exactly one space character. 
There will be no spaces in the beginning or at the end of the argument strings.

sentence = "it was a dark and stormy python"

print(first_word(sentence)) # it
print(second_word(sentence)) # was
print(last_word(sentence)) # python
'''


def first_word(sentence):
    # Find the position of the first space
    first_space_index = sentence.find(' ')

    if first_space_index != -1:
        # Extract the first word
        first_word = sentence[:first_space_index]
        return first_word
    else:
        return "The sentence does not have a first word."

def second_word(sentence):
    # Find the position of the first space
    first_space_index = sentence.find(' ')

    if first_space_index != -1:
        # Find the position of the second space after the first space
        second_space_index = sentence.find(' ', first_space_index + 1)

        if second_space_index != -1:
            # Extract the second word
            second_word = sentence[first_space_index + 1:second_space_index]
            return second_word
        else:
            # If there is no second space, return the word after the first space
            return sentence[first_space_index + 1:]
    else:
        return "The sentence does not have a second word."

def last_word(sentence):
    # Find the position of the last space
    last_space_index = sentence.rfind(' ')

    if last_space_index != -1:
        # Extract the last word
        last_word = sentence[last_space_index + 1:]
        return last_word
    else:
        return "The sentence does not have a last word."

sentence = "it was a dark and stormy python"
#sentence = "it was"

print(first_word(sentence))
print(second_word(sentence))
print(last_word(sentence))
