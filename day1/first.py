from math import *
def counts(num):
    if num==0:
        return 1
    else:
        return int(log10(num)+1)
def palindrom(num):
    result=0
    n=num
    while(num):
        digit=num%10
        result=result*10+digit
        num=num//10
    return n==result
def armstrong(num):
    node=len(str(num))
    n=num
    result=0
    while(num):
        digit=num%10
        result+=(digit**node)
        num=num//10
    return n==result
def factors(num):
    result=[]
    for i in range(1,int(sqrt(num)+1)):
        if num%i==0:
            result.append(i)
            if num//i!=i:
                result.append(num//i)
    return result
num=12345
result=counts(num)
print(result)