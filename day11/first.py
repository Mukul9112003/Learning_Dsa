matrix=[[1,2,3,4,5,6],[20,21,22,23,24,7],[19,32,33,34,25,8],[18,31,36,35,26,9],[17,30,29,28,27,10],[16,15,14,13,12,11]]
def display(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print(matrix[row][col],end=" ")
        print()
def spiral_matrix(matrix):
    result=[]
    left,top=0,0
    bottom,right=len(matrix)-1,len(matrix[0])-1
    while top<=bottom and left<=right:
        for i in range(left,right+1):
            result.append(matrix[top][i])
        top+=1
        for j in range(top,bottom+1):
            result.append(matrix[j][right])
        right-=1
        if top<=bottom:
            for i in range(right,left-1,-1):
                result.append(matrix[bottom][i])
            bottom-=1
        if left<right:
            for j in range(bottom,top-1,-1):
                result.append(matrix[j][left])
            left+=1
    return result
print(spiral_matrix(matrix))