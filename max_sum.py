def max_sum(nums, k):
    sum_window = sum(nums[:k])
    max_sum = sum_window

    for i in range(k, len(nums)):
        sum_window -= nums[i - k]
        sum_window += nums[i]
        max_sum = max(sum_window, max_sum)

    return max_sum