def cubrir(c2, c3, n):
	dp = [0 for i in range(n+1)] 
	dp[1] = dp[2] = min(c2,c3)

	for i in range(3, n+1):
		dp[1] = min(dp[i-1] + c2, dp[i-1] + c3, dp[i-2] + c2, dp[i-1] + c3, dp[i-3] + c3)

	return dp
print (cubrir(5, 7, 10))
