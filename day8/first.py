prices = [7, 2, 1, 5, 6, 4, 8]


def stock(prices):
    min_price = float("inf")
    max_profit = 0
    for i in range(len(prices)):
        min_price = min(prices[i], min_price)
        max_profit = max(max_profit, prices[i] - min_price)
    return max_profit


print(stock(prices))
nums = [5, 10, -3, -1, -10, 6]


def rearrange(nums):
    result = [0] * len(nums)
    pos_index = 0
    neg_index = 1
    for i in range(len(nums)):
        if nums[i] >= 0:
            result[pos_index] = nums[i]
            pos_index += 2
        else:
            result[neg_index] = nums[i]
            neg_index += 2
    return result


print(rearrange(nums))
nums = [1, 99, 101, 98, 2, 5, 3, 99, 100]


def largest_consecutive(nums):
    mapping_set = set(nums)
    max_count = 0
    for num in mapping_set:
        if num - 1 not in mapping_set:
            n = 1
            while num + 1 in mapping_set:
                n += 1
                num += 1
            max_count = max(max_count, n)
    return max_count


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def max_subarray_sum(nums):
    total = 0
    max_sum = float("-inf")
    for i in range(len(nums)):
        total += nums[i]
        max_sum = max(total, max_sum)
        total = max(total, 0)
    return max_sum


nums = [5, 9, 1, 2, 4, 15, 6, 3]


def two_sum(nums, target):
    mapping_index = {}
    for i in range(len(nums)):
        remaining = target - nums[i]
        if remaining in mapping_index:
            return i, mapping_index[remaining]
        mapping_index[nums[i]] = i
    return None


print(two_sum(nums, 13))
