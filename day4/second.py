def move_zero_to_end(nums):
    n=len(nums)
    if n==1:
        return 
    i=0
    while(i<n):
        if nums[i]==0:
            break
        i+=1
    j=i+1
    while(j<n):
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
        j+=1
def remove_duplicate(nums):
    n=len(nums)
    if n==1:
        return
    i=0
    j=i+1
    while(j<n):
        if nums[j]!=nums[i]:
            i+=1
            nums[i],nums[j]=nums[j],nums[i]
        j+=1
    return i+1    