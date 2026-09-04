import math 
def factor(num):
    result=[]
    for i in range(1,int(math.sqrt(num))+1):
        if num%i==0:
            result.append(i)
            if (num//i)!=i:
                result.append(num//i)
    return result
print(factor(36))
def bubble(nums):
    n=len(nums)
    for i in range(n-2,-1,-1):
        is_swap=False
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                is_swap=True
        if is_swap:
            break
nums=[1,3,2,5,4,9,7,6]
bubble(nums)
print(nums)
def merge(left,right):
    result=[]
    i=j=0
    m,n=len(left),len(right)
    while i<n and j<m:
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i<n:
        result.append(left[i])
        i+=1
    while j<m:
        result.append(right[j])
        j+=1
    return result
def merge_sort(nums):
    if len(nums)<=1:
        return nums
    mid=len(nums)//2
    left_arr=nums[:mid]
    right_arr=nums[mid:]
    left=merge_sort(left_arr)
    right=merge_sort(right_arr)
    return merge(left,right)
nums=[1,3,2,5,4,9,7,6]
print(merge_sort(nums))
def largest(nums):
    large=second=float("-inf")
    for  i in range(len(nums)):
        if nums[i]>large:
            second=large
            large=nums[i]
        if nums[i]>second and nums[i]!=large:
            second=nums[i]
    return large,second
nums=[1,3,2,5,4,9,7,6]
print(largest(nums))
def is_sort(nums):
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            return False
    return True
print(is_sort(nums))