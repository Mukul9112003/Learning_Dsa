def move_zeroes(nums):
    if len(nums)==1:
        return nums
    i=0
    while nums[i]!=0:
        i+=1
    if i==len(nums):
        return
    j=i+1
    while (j<len(nums)):
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
        j+=1
nums1=[1, 1,2,3,4,6,7]
nums2=[1,2,3,6,7,8,9,10]
def merge(nums1,nums2):
    m,n=len(nums1),len(nums2)
    i=j=0
    result=[]
    while i<m and j<n:
        if nums1[i]<=nums2[j]:
            if len(result)==0 or result[-1]!=nums1[i]:
                result.append(nums1[i])
            i+=1
        else:
            if len(result)==0 or result[-1]!=nums2[j]:
                result.append(nums2[j])
            j+=1
    while i<m:
        if len(result)==0 or result[-1]!=nums1[i]:
            result.append(nums1[i])
        i+=1
    while j<n:
        if len(result)==0 or result[-1]!=nums2[j]:
            result.append(nums2[j])
        j+=1
freq={x:0 for x in range(10)}
print(freq)