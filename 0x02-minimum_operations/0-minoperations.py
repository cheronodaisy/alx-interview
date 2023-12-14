#!/usr/bin/python3

def minOperations(n):
    if n == 1:
        return 0
    
    # Initialize an array to store minimum operations for each position
    dp = [0] * (n + 1)
    
    for i in range(2, n + 1):
        dp[i] = i  # Initialize with the maximum possible value
        
        # Iterate through factors of 'i' to find the minimum operations
        for j in range(2, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
    
    return dp[n]
