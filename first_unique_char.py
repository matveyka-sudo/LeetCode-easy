def first_unique_char(s):
    d = {}

    for char in s:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1

    for index, char in enumerate(s):
        if d[char] == 1:
            return index

    return -1