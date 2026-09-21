nums = [1, 99, 101, 98, 2, 5, 3, 00, 100]


def consecutive_method1(nums):
    n = len(nums)
    max_count = 0
    for i in range(n):
        num = nums[i]
        count = 1
        while num + 1 in nums:
            count += 1
            num += 1
        max_count = max(max_count, count)
    return max_count
def consecutive_method2(nums):
    nums.sort()
    count = 0
    max_count = 0
    last_previous = float("inf")
    for i in range(len(nums)):
        num = nums[i]
        if num - 1 == last_previous:
            count += 1
            last_previous = num
        if num != last_previous:
            count = 1
            last_previous = num
        max_count = max(max_count, count)
    return max_count
def consecutive_method3(nums):
    my_set = set(nums)
    longest = 0
    for num in my_set:
        if num - 1 not in my_set:
            count = 1
            while num + 1 in my_set:
                count += 1
                num = num + 1
            longest = max(longest, count)
    return longest


print(consecutive_method1(nums))
print(consecutive_method2(nums))
print(consecutive_method3(nums))
