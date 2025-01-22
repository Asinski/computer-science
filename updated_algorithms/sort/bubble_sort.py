def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

assert bubble_sort([0, 1, 2, -1, 9, 4, 3]) == [-1, 0, 1, 2, 3, 4, 9]
assert bubble_sort([9, 4, 3, 2]) == [2, 3, 4, 9]
assert bubble_sort([4, 1, 2, 3]) == [1, 2, 3, 4]
