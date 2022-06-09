class Solution:
    
    import math
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        #code here
        l,r=max(A),sum(A)
        while l<=r:
            mid=l+(r-l)//2
            if self.isPossible(A,N,M,mid):
                r=mid-1
            else:
                l=mid+1
        return r+1        
        
    # Partition Valid Methods;    
    def isPossible(self,A, n, M, mid):
        c,summ,i=1,0,0
        for i in range(n):
            if(summ+A[i]<=mid):
                summ+=A[i]
            else:
                c+=1
                summ=A[i]
        return c<=M      


#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends