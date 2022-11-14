#User function Template for python3
from collections import Counter
class Solution:
    def isProduct(self, arr, n, x):
        # code here
        map = Counter(arr)
        for i in arr:
            if i!=0:
                s = x//i
                if s in map and s*i==x:
                    return True
                    break
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.isProduct(arr, n, x)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends
