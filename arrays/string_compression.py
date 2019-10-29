"""


Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'.
For this problem, you can falsely "compress" strings of single or double letters.
For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.

"""


def compress(s):
    s_len = len(s)
    if s_len == 0:
        return ""
    final_output = ""
    i = 0
    while i < s_len:

        start_letter = s[i]
        count = 1

        while i + 1 < s_len and start_letter == s[i + 1]:
            count += 1
            i += 1

        final_output += (start_letter + str(count))
        i += 1

    return final_output


print compress('AAAABBBBCCCCCDDEEEE')
