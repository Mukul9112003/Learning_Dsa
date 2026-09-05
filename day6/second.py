def max_consecutive_ones(nums):
    max_count=count=0
    for i in range(len(nums)):
        if nums[i]==1:
            count+=1
        else:
            max_count=max(count,max_count)
            count=0
    return max(count,max_count)
nums=[1,2,1,1,1,0,3,4,1,1,1,1]
print(max_consecutive_ones(nums))

def two_sum(nums,target):
    freq={}
    for i in range(len(nums)):
        remainder=target-nums[i]
        if remainder in freq:
            return (freq[remainder],i)
        freq[nums[i]]=i
nums=[1,2,1,1,1,0,3,4,1,1,1,1]
print(two_sum(nums, target=6))