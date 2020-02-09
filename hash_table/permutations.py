
def permutations(string, step=0):
    if step == len(string):
        return "".join(string)
    for i in range(step, len(string)):
        string_copy = list(string)
        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
        # recurse on the portion of the string that has not been swapped yet
        permutations(string_copy, step + 1)


print(permutations('abc'))


def permute(seq):
    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i + 1:]
            for x in permute(rest):
                yield seq[i:i + 1] + x


print(list(permute('abc')))
