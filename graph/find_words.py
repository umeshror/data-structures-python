grid1 = [['E', 'L', 'E', 'K', 'T', 'R', 'A', 'H', 'T', 'H', 'O', 'R', 'G', 'V'],
         ['S', 'I', 'L', 'V', 'E', 'R', 'A', 'O', 'R', 'W', 'T', 'N', 'S', 'H'],
         ['A', 'U', 'A', 'U', 'A', 'W', 'R', 'E', 'H', 'S', 'I', 'N', 'U', 'P'],
         ['H', 'N', 'E', 'R', 'K', 'C', 'T', 'N', 'W', 'H', 'A', 'M', 'R', 'R'],
         ['A', 'F', 'T', 'E', 'H', 'S', 'I', 'I', 'T', 'M', 'A', 'S', 'F', 'A'],
         ['I', 'C', 'Y', 'M', 'I', 'L', 'D', 'R', 'R', 'N', 'C', 'A', 'E', 'A'],
         ['I', 'E', 'I', 'M', 'A', 'O', 'I', 'E', 'E', 'A', 'E', 'R', 'R', 'L'],
         ['W', 'W', 'Y', 'T', 'W', 'N', 'D', 'V', 'R', 'M', 'G', 'E', 'I', 'O'],
         ['I', 'N', 'V', 'I', 'D', 'I', 'B', 'L', 'E', 'G', 'A', 'G', 'R', 'O'],
         ['T', 'D', 'H', 'S', 'P', 'A', 'E', 'O', 'H', 'D', 'C', 'N', 'O', 'P'],
         ['C', 'I', 'O', 'S', 'K', 'T', 'T', 'Z', 'T', 'G', 'E', 'A', 'N', 'D'],
         ['H', 'F', 'K', 'O', 'K', 'P', 'R', 'N', 'N', 'L', 'K', 'R', 'M', 'A'],
         ['E', 'B', 'W', 'O', 'M', 'A', 'N', 'P', 'A', 'E', 'U', 'T', 'A', 'E'],
         ['U', 'O', 'F', 'A', 'L', 'C', 'O', 'N', 'P', 'F', 'L', 'S', 'N', 'D']]


words1 = ['ANTMAN', 'DAREDEVIL ', 'DEADPOOL', 'ELEKTRA', 'HAWKEYE', 'PUNISHER',
         'THING']


grid = [['T', 'R', 'A', 'P'],
        ['C', 'A', 'R', 'D'],
        ['F', 'A', 'C', 'T'],
        ['D', 'A', 'R', 'T']];''

words = ['CAT', 'DOG', 'FACT']

def word_seek(grid, words):
    founds = []

    for word in words:
        found = False
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if not found and grid[i][j] == word[0] and dfs(grid, i, j, \
                        chars_found=0, word=word):
                    found = True
                    founds.append("{} {} {}".format(word, i, j))
        if not found:
            founds.append("{} {} {}".format(word, -1, -1))

    return founds


def dfs(grid, i, j, chars_found, word, direction = None):
    if chars_found == len(word):
        return True

    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] != \
            word[chars_found]:
        return False

    temp = grid[i][j]
    grid[i][j] = ''  # make it empty string so it wont be repeated
    go_up = go_right_up = go_right = go_down_right = go_down = go_left_down =\
        go_left = go_left_up = False

    if direction in [None, "go_right"]:
        go_right = dfs(grid, i, j + 1, chars_found + 1, word, "go_right")

    if direction in [None , "go_left"]:
        go_left = dfs(grid, i, j - 1, chars_found + 1, word, "go_left")

    if direction in [None , "go_up"]:
        go_up = dfs(grid, i - 1, j, chars_found + 1, word, "go_up")

    if direction in [None , "go_down"]:
        go_down = dfs(grid, i + 1, j, chars_found + 1, word, "go_down")

    if direction in [None , "go_right_up"]:

        go_right_up = dfs(grid, i - 1, j + 1, chars_found + 1, word,
                          "go_right_up")

    if direction in [None , "go_down_right"]:
        go_down_right = dfs(grid, i + 1, j + 1, chars_found + 1, word,
                            "go_down_right")

    if direction in [None , "go_left_down"]:
        go_left_down = dfs(grid, i + 1, j - 1, chars_found + 1, word,
                           "go_left_down")

    if direction in [None , "go_left_up"]:
        go_left_up = dfs(grid, i - 1, j - 1, chars_found + 1, word,
                         "go_left_up")

    found = go_up or go_right_up or go_right or go_down_right or go_down or go_left_down or go_left or go_left_up

    grid[i][j] = temp
    return found


founds = word_seek(grid1, words=words1)
if founds:
    for f in founds:
        print f
        print ""
"""
Expected Output
Download
ANTMAN 2 0
DAREDEVIL 13 13
DEADPOOL 13 13
ELEKTRA 0 0
HAWKEYE 0 7
PUNISHER 2 13
THING 4 8
WITCH 7 0
"""