def next_palin_number(number):
    # Convert the number to a list of its digits.
    number = list(str(number))
    # Initialize two indices for comparing symmetric digits.
    i = 0
    j = len(number) - 1
    while i < j:
        # If the digits are different:
        if number[i] != number[j]:
            # If the lower-power digit is greater than the higher-power digit:
            if int(number[j]) > int(number[i]):
                number[j - 1] = str(int(number[j - 1]) + 1)
                number[j] = number[i]
            else:
                number[j] = number[i]
        i += 1
        j -= 1
    # Concatenate and return the result.
    return "".join(number)

print(next_palin_number(125))