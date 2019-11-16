"""
Given a dictionary, and two words 'start' and 'target' (both of same length).
 Find length of the smallest chain from 'start' to 'target' if it exists, such
 that adjacent words in the chain only differ by one character and each word
 in the chain is a valid word i.e., it exists in the dictionary. It may be
 assumed that the 'target' word exists in dictionary and length of
 all dictionary words is same.

Input:
begin_word = "hit",
end_word = "cog",
words = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
"""


import collections


def word_ladder(begin_word, end_word, words):
    """
    :type begin_word: str
    :type end_word: str
    :type words: List[str]
    :rtype: int
    """

    if end_word not in words or not end_word or not begin_word or not words:
        return 0

    # Since all words are of same length.
    str_len = len(begin_word)

    # Dictionary to hold combination of words that can be formed,
    # from any given word. By changing one letter at a time.
    all_combo_dict = collections.defaultdict(list)
    for word in words:
        for i in range(str_len):
            # Value is a list of words which have the same intermediate generic word.
            all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
            # {"do*": ["dog", "dot"]}

    # Queue for BFS
    queue = collections.deque([(begin_word, 1)])
    # Visited to make sure we don't repeat processing same word.
    visited_words = set([begin_word])
    while queue:
        current_word, level = queue.popleft()
        for i in range(str_len):
            # Intermediate words for current word
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]

            # Next states are all the words which share the same intermediate state.
            next_words = all_combo_dict[intermediate_word]
            for word in next_words:
                # If at any point if we find what we are looking for
                # i.e. the end word - we can return with the answer.
                if word == end_word:
                    return level + 1
                # Otherwise, add it to the BFS Queue. Also mark it visited
                if word not in visited_words:
                    queue.append((word, level + 1))
                    visited_words.add(word)
            all_combo_dict[intermediate_word] = []
    return 0

word_list = ["hot","dot","dog","lot","log","cog"]
begin_word = "hit"
end_word = "cog"


print word_ladder(begin_word, end_word, word_list)






