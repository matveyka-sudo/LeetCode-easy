def min_subarray_len(nums, target):
    left = 0
    window_sum = 0
    min_len = len(nums)
    for right in range(len(nums)):
        window_sum = sum(nums[left:right])
        while window_sum >= target:
            current_len = right - left
            min_len = min(min_len, current_len)
            left += 1
            window_sum = sum(nums[left:right])
    return min_len