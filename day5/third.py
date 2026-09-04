def k_rotate_method1(nums,rotation):
    for i in range(rotation):
        e=nums.pop()
        nums.insert(0,e)
nums=[1,2,3,4,5,6,7,8,9]
k_rotate_method1(nums,3)
print(nums)
def reverse1(nums,left,right):
    while(left<right):
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
def reverse(nums,left,right):
    if left>=right:
        return
    nums[left],nums[right]=nums[right],nums[left] 
    return reverse(nums,left+1,right-1)
def rotate_method_2(nums,rotate):
    n=len(nums)
    reverse(nums,n-rotate,n-1)
    reverse(nums,0,n-rotate-1)
    reverse(nums,0,n-1)
nums=[1,2,3,4,5,6,7,8,9]
rotate_method_2(nums,3)
print(nums)