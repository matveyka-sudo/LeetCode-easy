def contains_duplicate(nums):
    s = set()
    for number in nums:
        if number in s:
            return True
        s.add(number)
    return False