def is_anagram(s, t):
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for i in t:
        if i not in d:
            return False
        else:
            d[i] -= 1
    for i in d.keys():
        if d[i] != 0:
            return False
    return True