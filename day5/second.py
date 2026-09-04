def remove_duplicate_method1(nums):
    dic={}
    for num in nums:
        dic[num]=0
    j=0
    n=len(nums)
    for num in dic:
        nums[j]=num
        j+=1
    return j
nums=[1,1,1,2,3,4,4,7,9,9,9,10]
print(remove_duplicate_method1(nums))
def remove_duplicate_method2(nums):
    n=len(nums)
    if n<=1:
        return n
    i=0
    j=i+1
    while j<n:
        if nums[j]!=nums[i]:
            i+=1
            nums[i],nums[j]=nums[j],nums[i]
        j+=1
    return i+1
nums=[1,1,1,2,3,4,4,7,9,9,9,10]
print(remove_duplicate_method2(nums))
nums=[1,1,1,2,3,4,4,7,9,9,9,10]
def roate_last_place_method1(nums):
    temp=nums[-1]
    n=len(nums)
    for i in range(n-2,-1,-1):
        nums[i+1]=nums[i]
    nums[0]=temp
roate_last_place_method1(nums)
print(nums)
def rotate_last_place_method2(nums):
    n=len(nums)
    nums[:]=[nums[n-1]] + nums[0:n-1]
nums=[1,1,1,2,3,4,4,7,9,9,9,10]
rotate_last_place_method2(nums)
print(nums)