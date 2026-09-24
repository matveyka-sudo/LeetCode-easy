def sorted_squares(nums):
    result = [0] * len(nums)

    left = 0
    right = len(nums) - 1
    pos = len(nums) - 1

    while left <= right:
        if nums[left] ** 2 < nums[right] ** 2:
            result[pos] = nums[right] ** 2
            right -= 1
        else:
            result[pos] = nums[left] ** 2
            left += 1

        pos -= 1

    return result