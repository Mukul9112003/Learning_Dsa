def bubble_sort(num):
    for i in range(len(num)-2,-1,-1):
        is_swap=False
        for j in range(0,i+1):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]
                is_swap=True
        if is_swap==False:
            break
