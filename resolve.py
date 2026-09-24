def reverse_vowels(s):
    chars = list(s)
    left = 0
    right = len(chars) - 1
    while left < right:
        if chars[left] in "aeiouAEIOU" and chars[right] in "aeiouAEIOU":
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        elif chars[left] in "aeiouAEIOU" and chars[right] not in "aeiouAEIOU":
            right-=1
        elif chars[left] not in "aeiouAEIOU" and chars[right] in "aeiouAEIOU":
            left+=1
        else:
            left+=1
            right -= 1
    return "".join(chars)