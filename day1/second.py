freq_dic={}
num=[1,2,3,4,5,6,7,8,9]
n=len(num)
for i in range(n):
    freq_dic[num[i]]=freq_dic.get(num[i],0)+1
print(freq_dic)