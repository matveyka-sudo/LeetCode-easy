def is_isomorphic(s, t):
    d = {}
    d1 = {}

    for char_s, char_t in zip(s, t):
        if char_s in d:
            if d[char_s] != char_t:
                return False
        else:
            d[char_s] = char_t

        if char_t in d1:
            if d1[char_t] != char_s:
                return False
        else:
            d1[char_t] = char_s

    return True