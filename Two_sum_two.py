def two_sum(nums, target):
    d = {}
    for index, number in enumerate(nums):
        need = target - number
        if need in d:
            return d[need], index
        else:
            d[number] = index