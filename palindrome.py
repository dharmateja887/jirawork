class Solution():
    def ispalindrome(self,x):
        if x<0:
            return False
        q=str(x)
        rev: str=q[::-1]
        return q == rev
w=Solution()
print(w.ispalindrome(121))
print(w.ispalindrome(-121))
print(w.ispalindrome(10))