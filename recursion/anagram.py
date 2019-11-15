def find_anagram(str1, str2):
    combinations = get_combinations(str1)
    for result in combinations:
        if result == str2:
            return True
    return False


def get_combinations(string):
    combinations = set()

    if len(string) == 1:
        combinations.add(string)
        return combinations

    for i in range(len(string)):
        other_chars = ''
        for j in range(len(string)):
            if j != i:
                other_chars += string[j]
        for result in get_combinations(other_chars):
            combinations.add(string[i] + result)
    return combinations


print(find_anagram("bcd", "cbd"))
