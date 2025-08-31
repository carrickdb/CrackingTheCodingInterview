def stairWays(n):
    # dp = [0,0,1]
    # for i in range(n):
    #     dp[0], dp[1], dp[2] = dp[1], dp[2], sum(dp)
    # return dp[-1]
    if n < 0:
        return 0
    if n==0:
        return 1
    return stairWays(n-1) + stairWays(n-2) + stairWays(n-3)



for i in range(6):
    print(stairWays(i))