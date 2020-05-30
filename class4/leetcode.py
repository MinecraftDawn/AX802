class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False




s = "rat"
t = "car"
ans = Solution().isAnagram(s, t)

print(ans)