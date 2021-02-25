#
# @lc app=leetcode.cn id=877 lang=python3
#
# [877] 石子游戏
#
# https://leetcode-cn.com/problems/stone-game/description/
#
# algorithms
# Medium (71.64%)
# Likes:    217
# Dislikes: 0
# Total Accepted:    28.3K
# Total Submissions: 39.1K
# Testcase Example:  '[5,3,4,5]'
#
# 亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。
# 
# 游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。
# 
# 亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。
# 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。
# 
# 假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false 。
# 
# 
# 
# 示例：
# 
# 输入：[5,3,4,5]
# 输出：true
# 解释：
# 亚历克斯先开始，只能拿前 5 颗或后 5 颗石子 。
# 假设他取了前 5 颗，这一行就变成了 [3,4,5] 。
# 如果李拿走前 3 颗，那么剩下的是 [4,5]，亚历克斯拿走后 5 颗赢得 10 分。
# 如果李拿走后 5 颗，那么剩下的是 [3,4]，亚历克斯拿走后 4 颗赢得 9 分。
# 这表明，取前 5 颗石子对亚历克斯来说是一个胜利的举动，所以我们返回 true 。
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= piles.length <= 500
# piles.length 是偶数。
# 1 <= piles[i] <= 500
# sum(piles) 是奇数。
# 
# 
#

# @lc code=start
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        self.dp_table = defaultdict( int )
        
        def maximize_score_gap( piles, left, right):
            
            if left == right:
                # Base case
                # only one pile of stone remains
                return piles[left]
            
            if (left, right) in self.dp_table:
                # Directly return if this case has been computed before
                return self.dp_table[ (left, right)] 
            
            # Use optimal substructure to compute maximized score gap
            choose_left = piles[left] - maximize_score_gap( piles, left+1, right)
            choose_right = piles[right] - maximize_score_gap( piles, left, right-1)
            
            # update DP table
            self.dp_table[ (left,right) ] = max( choose_left, choose_right )
            
            return self.dp_table[ (left,right) ]
        score_gap_for_alex = maximize_score_gap( piles, left = 0, right = len(piles)-1 )
        
        return score_gap_for_alex > 0
# @lc code=end

定义二维数组 \textit{dp}dp，其行数和列数都等于石子的堆数，\textit{dp}[i][j]dp[i][j] 表示当剩下的石子堆为下标 ii 到下标 jj 时，当前玩家与另一个玩家的石子数量之差的最大值，注意当前玩家不一定是先手 \text{Alex}Alex。

只有当 i \le ji≤j 时，剩下的石子堆才有意义，因此当 i>ji>j 时，\textit{dp}[i][j]=0dp[i][j]=0。

当 i=ji=j 时，只剩下一堆石子，当前玩家只能取走这堆石子，因此对于所有 0 \le i < \textit{nums}.\text{length}0≤i<nums.length，都有 \textit{dp}[i][i]=\textit{piles}[i]dp[i][i]=piles[i]。

当 i<ji<j 时，当前玩家可以选择取走 \textit{piles}[i]piles[i] 或 \textit{piles}[j]piles[j]，然后轮到另一个玩家在剩下的石子堆中取走石子。在两种方案中，当前玩家会选择最优的方案，使得自己的石子数量最大化。因此可以得到如下状态转移方程：

\textit{dp}[i][j]=\max(\textit{piles}[i] - \textit{dp}[i+1][j], \textit{piles}[j] - \textit{dp}[i][j-1])
dp[i][j]=max(piles[i]−dp[i+1][j],piles[j]−dp[i][j−1])

最后判断 \textit{dp}[0][\textit{piles}.\text{length}-1]dp[0][piles.length−1] 的值，如果大于 00，则 \text{Alex}Alex 的石子数量大于 \text{Lee}Lee 的石子数量，因此 \text{Alex}Alex 赢得比赛，否则 \text{Lee}Lee 赢得比赛。

 
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        length = len(piles)
        dp = [[0] * length for _ in range(length)]
        for i, pile in enumerate(piles):
            dp[i][i] = pile
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        return dp[0][length - 1] > 0
 

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        length = len(piles)
        dp = [0] * length
        for i, pile in enumerate(piles):
            dp[i] = pile
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])
        return dp[length - 1] > 0

 时间复杂度：O(n^2)O(n 
2
 )，其中 nn 是数组的长度。需要计算每个子数组对应的 \textit{dp}dp 的值，共有 \frac{n(n+1)}{2} 
2
n(n+1)
​	
  个子数组。

空间复杂度：O(n)O(n)，其中 nn 是数组的长度。空间复杂度取决于额外创建的数组 \textit{dp}dp，如果不优化空间，则空间复杂度是 O(n^2)O(n 
2
 )，使用一维数组优化之后空间复杂度可以降至 O(n)O(n)。
 