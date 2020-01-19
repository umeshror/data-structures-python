import re


def find_largest_sol1(strng):
    """
    :param strng: String can consists special chars and nums
    :return: Largest valid string which will have chars only
    """
    if not strng:
        return
    word = ""
    words = []
    strng += " "
    for s in strng:
        if s != ' ':
            word += s
        else:
            # to consider nums and underscore ^[a-zA-Z0-9_]*$
            if re.match("^[a-zA-Z]*$", word):
                words.append(word)
            word = ""
    if not words:
        return None
    largest = words[0]

    for k in range(0, len(words)):
        if len(largest) < len(words[k]):
            largest = words[k]
    return largest


def find_largest_sol2(strng):
    """
    :param strng: String can consists special chars and nums
    :return: Largest valid string which whill have chars only
    """
    # split letters by space
    words = strng.split(' ')
    if not words:
        return

    largest = ""
    for word in words:
        if re.match("^[a-zA-Z]*$", word):
            if len(largest) < len(word):
                largest = word
    return largest


print(find_largest_sol1('fun&!! time'))
print(find_largest_sol2('fun&!! time'))
