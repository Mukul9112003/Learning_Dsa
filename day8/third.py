def reverse(nums,left,right):
    if left>=right:
        return
    nums[left],nums[right]=nums[right],nums[left]
    return reverse(nums,left+1,right-1)
def rotate(nums,target):
    n=len(nums)
    reverse(nums,n-target,n-1)
    reverse(nums,0,n-target-1)
    reverse(nums,0,n-1)
def remove_duplicate(nums):
    n=len(nums)
    freq_map={}
    for i in range(n):
        