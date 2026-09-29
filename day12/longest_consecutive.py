def method1(nums):
    count=0
    max_count=0
    for num in nums:
        n=num
        count=1
        while n+1 in nums:
            count+=1
            n+=1
        max_count=max(max_count,count)
    return max_count
def method2(nums):
    nums.sort()
    count=max_count=0
    last_previous=float("inf")
    for num in nums:
        if num-1==last_previous:
            count+=1
        else:
            count=1
        last_previous=num
        max_count=max(max_count,count)
    return max_count
def method3(nums):
    my_set=set(nums)
    longest=0
    for num in my_set:
        if num-1 not in my_set:
            n=num
            count=1
            while n+1 in my_set:
                count+=1
                n+=1
            longest=max(longest,count)
    return longest
nums=[1,99,101,98,2,5,3,100,1,1]
print(method1(nums))
print(method2(nums))
print(method3(nums))