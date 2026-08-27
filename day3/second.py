def largest(nums):
    large=second_large=float("-inf")
    for i in nums:
        if large<i:
            large=i
            second_large=large
        elif second_large<i and large!=second_large:
            second_large=i
    return second_large
def check_sorted(nums):
    for j in range(0,len(nums)-1):
        if nums[j]>nums[j+1]:
            return False
    return True
nums=[1,2,3,4,5,6,7,8,9]
print(check_sorted(nums))
print(largest(nums))