'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # make sure word is at least 2 letters long
    if len(word) < 2:
        return 0

    # if word contains th
    if word[:2] == "th":

        return 1 + count_th(word[1:])
    else:
        return 0 + count_th(word[1:])


# my own test
print(count_th("thethethe"))
# print(count_th("cat"))
# print(count_th("I"))
