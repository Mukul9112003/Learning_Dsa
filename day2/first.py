import math
def factor(num):
    n=len(num)
    result=[]
    for i in range(int(math.sqrt(n))):
        if num %i==0:
            result.append(i)
            if num//i!=i:
                result.append(num//i)
    result.sort()
    return result
def counting_head(num):
    if num==0:
        return
    counting_head(num-1)
    print(num)
#counting_head(5)
def reverse_counting_head(num,i=1):
    if i==(num+1):
        return
    reverse_counting_head(num,i+1)
    print(i)
#reverse_counting_head(5)
def counting_tail(num,i=1):
    if i==(num+1):
        return
    print(i)
    counting_tail(num,i+1)
counting_tail(5)
def reverse_counting_tail(num):
    if num==0:
        return
    print(num)
    reverse_counting_head(num-1)
reverse_counting_tail(5)