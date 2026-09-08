def buy_sell(nums):
    n=len(nums)
    max_profit=0
    buy=float("inf")
    for i in range(n):
        buy=min(buy,nums[i])
        max_profit=max(max_profit,nums[i]-buy)
    return max_profit
price=[7,2,1,5,6,4,8]
print(buy_sell(price))