def contains_nearby_duplicate(nums, k):
    d = {}

    for index, number in enumerate(nums):
        if number in d:
            distance = index - d[number]

            if distance <= k:
                return True

        d[number] = index

    return False