nums = [[5, 20, 3], [7, -10, 9], [1, -52, 6]]


def upper_triangle(nums):
    row = len(nums)
    col = len(nums[0])
    for i in range(row):
        for j in range(col):
            if i > j:
                nums[i][j] = "*"


upper_triangle(nums)
print(nums)
