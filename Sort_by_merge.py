def merge_sort(my_arr):
    if len(my_arr) <= 1:
        return my_arr
    mid = len(my_arr) // 2
    left, right = merge_sort(my_arr[:mid]), merge_sort(my_arr[mid:])
    return merge(left, right, my_arr.copy())


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor +=1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor +=1
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]
    return merged


my_arr = [9, 3, 41, 67, 2, 19, 0, 84]

print(merge_sort(my_arr))
