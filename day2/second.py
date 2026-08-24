n=[5,3,2,2,1,5,5,7,5,10,111,654]
hash_list=[0]*11
for num in n:
    if num<1 or num>10:
        print(0)
    else:
        hash_list[num]=hash_list[num]+1
print(hash_list)

def reverse_array(nums,left,right):
    if left>=right:
        return
    nums[left],nums[right]=nums[right],nums[left]
    reverse_array(nums,left+1,right-1)
reverse_array(n,0,len(n)-1)
print(n)