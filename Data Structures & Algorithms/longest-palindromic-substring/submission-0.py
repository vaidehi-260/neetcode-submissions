class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        def expand(l, r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        for i in range(len(s)):
            odd = expand(i, i)
            if len(odd)>len(ans):
                ans = odd
            even = expand(i, i+1)
            if len(even)>len(ans):
                ans = even
        return ans