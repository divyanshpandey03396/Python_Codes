#User function Template for python3
class Solution:
    def isPalindrome(self, S):
        # code here
        left,right=0,len(S)-1
        while left<=right :
          if left==right:
            return 1
          elif S[left]!=S[right] :
            return 0 
          else:
            left+=1
            right-=1
        return 1   
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.isPalindrome(S)
        print(answer)

# } Driver Code Ends