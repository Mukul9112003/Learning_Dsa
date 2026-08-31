def right_rotate_one_place(nums):
    n=len(nums)
    nums[:]=nums[n-1]+nums[:n-1]
#method 2:
def right_rotate(nums):
    n=len(nums)
    temp=nums[n-1]
    for i in range(n-2,-1,-1):
        nums[i+1]=nums[i]
    nums[0]=temp
def reverse(nums,left,right):
    if left>right:
        return
    nums[left],nums[right]=nums[right],nums[left]
    return reverse(nums,left+1,right-1)
def right_rotate_k(nums,k):
    n=len(nums)
    reverse(nums,n-k,n-1)
    reverse(nums,0,n-k-1)
    reverse(nums,0,n-1)
def right_rotate_k_place(nums,k):
    n=len(nums)
    nums[:]=nums[n-k:]+nums[0:n-k]
