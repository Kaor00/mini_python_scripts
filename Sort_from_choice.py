def selection_sort(nums):
    for i in range(len(nums)):
        minimum = i

        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minimum]:
                minimum = j

        nums[minimum], nums[i] = nums[i], nums[minimum]
    return nums


nums = [175, 8, 4, 83, 12, 3]

print(selection_sort(nums))
