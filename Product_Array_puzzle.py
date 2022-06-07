#User function Template for python3

class Solution:
    def productExceptSelf(self, nums, n):
        #code here
       ans=[]
       p=1
       k=1
       if nums.count(0)<=1:
           for i in range(n):
               p=p*nums[i]
               if nums[i]!=0:
                   k=k*nums[i]
           for i in range(n):
               if nums[i]!=0:
                   ans.append(p//nums[i])
               else:
                   ans.append(k)
           return ans
       else:
           return [0]*n
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends