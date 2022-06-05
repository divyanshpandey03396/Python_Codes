#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
         
        ans=[]
        for i in range(n):
            if arr[abs(arr[i]) - 1]<0 :
                ans.append(abs(arr[i]))
            else :
                arr[abs(arr[i]) - 1]*=-1
        for i in range(n):
            if arr[i]>0:
                ans.append(i+1)
        
        return ans
         
#{ 
#  Driver Code Starts
#Initial Template for Python 

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends