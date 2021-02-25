
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_len, p_len = len(s), len(p)
        i, j, star, i_index = 0, 0, -1, 0
        while i < s_len:
            if j < p_len and (p[j] == '?' or p[j] == s[i]):
                i += 1
                j += 1
            elif j < p_len and p[j] == '*':
                star = j
                j += 1
                i_index = i
            elif star != -1:
                j = star + 1
                i_index += 1
                i = i_index
            else:
                return False

        while j < p_len and p[j] == '*':
            j += 1

        return j == p_len


if __name__ == "__main__":
    s = "aa"
    p = "*"
    print(Solution().isMatch(s, p))


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False]*(len(s)+1) for i in range(len(p)+1)]
        dp[0][0] = True
        for i in range(1, len(p)+1):
            if p[i-1] == '*':
                dp[i][0] = dp[i-1][0]
        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):
                if p[i-1] == s[j-1] or p[i-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                else:
                    if p[i-1] == '*':
                        dp[i][j] = dp[i][j-1]
                        dp[i][j] = dp[i][j] or dp[i-1][j]
        return dp[-1][-1]