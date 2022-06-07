#User function Template for python3

class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        
        dp = [-1 for _ in range(n+1)]
    
        def solve(arr, n):
            if n < 0:
                return 0
            if dp[n] != -1:
                return dp[n]
            t1 = arr[n]+solve(arr, n-2)
            t2 = solve(arr, n-1)
            dp[n] = max(t1, t2)
            return dp[n]
        return solve(a, n-1)
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends