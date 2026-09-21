nums = [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1]


def consecutive_ones(nums):
    max_count = count = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            max_count = max(count, max_count)
            count = 0
    return max(max_count, count)


print(consecutive_ones(nums))
nums1 = [1, 1, 1, 2, 4, 6, 7]
nums2 = [1, 2, 3, 6, 7, 8, 9, 10]


def merge_two_sorted(nums1, nums2):
    m, n = len(nums1), len(nums2)
    i = j = 0
    result = []
    while i < m and j < n:
        if nums1[i] < nums[j]:
            if result[-1] != nums1[i] or len(result) == 0:
                result.append(nums1[i])
                i += 1
        else:
            if result[-1] != nums2[j] or len(result) == 0:
                result.append(nums2[j])
                j += 1
    while i < m:
        if result[-1] != nums1[i] or len(result) == 0:
            result.append(nums1[i])
            i += 1
    while j < n:
        if result[-1] != nums2[j] or len(result) == 0:
            result.append(nums2[j])
            j += 1
    return result


nums = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]


def move_zeroes(nums):
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            break
        i += 1
    if i == len(nums) - 1:
        return
    j = i + 1
    while j < len(nums):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1


move_zeroes(nums)
print(nums)
