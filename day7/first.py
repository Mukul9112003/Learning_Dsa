nums=[-2,1,-3,4,-1,2,1,-5,4]
def max_subarray(nums):
    n=len(nums)
    total=0
    max_sum=float("-inf")
    for i in range(n):
        total+=nums[i]
        max_sum=max(max_sum,total)
        if total<0:
            total=0
    return max_sum
print(max_subarray(nums))