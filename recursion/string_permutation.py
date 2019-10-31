"""


Given a string, write a function that uses recursion to output a list of all the
 possible permutations of that string.

For example,
s='abc' the function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

Note: If a character is repeated, treat each occurence as distinct, for example
an input of 'xxx' would return a list with 6 "versions" of 'xxx'
"""


def permute(s):
    """
    e.g. abc

    a b c
    a c b

    b a c
    b c a

    c a b
    c b a

    """
    output = []
    if len(s) <= 1:
        return s

    for i, letter in enumerate(s):
        # strip current letter from s and find perms on new string

        new_s = s[:i] + s[i + 1:]

        permutes = permute(new_s)

        for perm in permutes:
            output.append(letter + perm)

    return output


print(permute("abcd"))
