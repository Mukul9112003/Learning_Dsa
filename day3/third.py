nums=[1,1,1,2,3,4,4,7,9,9,9,10]
def duplicate(nums):
    freq_mapping={}
    n=len(nums)
    for i in range(0,n):
        freq_mapping[nums[i]]=0
    j=0
    for i in freq_mapping:
        nums[j]=i
        j+=1
    return j
def optimal_way(nums):
    n=len(nums)
    if n==1:
        return 1
    i=0
    j=i+1
    while j<n:
        if nums[i]!=nums[j]:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
        j+=1
    return i+1
print(optimal_way(nums))