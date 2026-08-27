def reverse(nums,left,right):
    while(left<right):
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
def reverse_with_recussion(nums,left,right):
    if left>=right:
        return
    nums[left],nums[right]=nums[right],nums[left]
    reverse_with_recussion(nums,left+1,right-1)
def palindrome_with_recussion(s,left,right):
    if left>=right:
        return True
    if s[left]!=s[right]:
        return False
    return palindrome_with_recussion(s,left+1,right-1)
def palindrome(s,left,right):
    while left<=right:
        if s[left]!=s[right]:
            return False
        left+=1
        right+=1
    return True
def bubble(nums):
    n=len(nums)
    for i in range(n-2,-1,-1):
        is_swap=False
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                is_swap=True
        if is_swap==False:
            break