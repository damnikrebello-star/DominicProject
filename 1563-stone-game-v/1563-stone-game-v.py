class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        if n == 1:
            return 0
            
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]
        maxL = [[0] * n for _ in range(n)]
        maxR = [[0] * n for _ in range(n)]

        for i in range(n):
            maxL[i][i] = stoneValue[i]
            maxR[i][i] = stoneValue[i]


        for i in range(n - 1, -1, -1):
            mid = i
            for j in range(i + 1, n):
                total_sum = prefix[j + 1] - prefix[i]
                

                while mid < j - 1 and 2 * (prefix[mid + 2] - prefix[i]) <= total_sum:
                    mid += 1

                left_sum = prefix[mid + 1] - prefix[i]
                
                if 2 * left_sum == total_sum:

                    dp[i][j] = max(maxL[i][mid], maxR[mid + 1][j])
                elif 2 * left_sum < total_sum:
     
                    res = maxL[i][mid]
                    if mid + 2 <= j:
                        res = max(res, maxR[mid + 2][j])
                    dp[i][j] = res
                else: 
         
                    dp[i][j] = maxR[i + 1][j]

                maxL[i][j] = max(maxL[i][j - 1], dp[i][j] + total_sum)
                maxR[i][j] = max(maxR[i + 1][j], dp[i][j] + total_sum)

        return dp[0][n - 1]