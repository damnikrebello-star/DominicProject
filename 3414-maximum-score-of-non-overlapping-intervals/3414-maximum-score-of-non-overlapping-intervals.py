import bisect
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = [(intervals[i][0], intervals[i][1], intervals[i][2], i) for i in range(n)]
        
        arr.sort(key=lambda x: (x[1], x[0], x[3]))

        R_arr = [x[1] for x in arr]
        
        dp = [[(-1, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = (0, ())
            
        for i in range(1, n + 1):
            l, r, w, idx = arr[i - 1]
            
            prev_idx = bisect.bisect_left(R_arr, l)
            
            for k in range(1, 5):
                best_state = dp[i - 1][k]
                
                prev_score, prev_tuple = dp[prev_idx][k - 1]
                if prev_score != -1:
                    take_score = prev_score + w

                    take_tuple = tuple(sorted(prev_tuple + (idx,)))
                    if take_score > best_state[0] or (take_score == best_state[0] and take_tuple < best_state[1]):
                        best_state = (take_score, take_tuple)
                        
                dp[i][k] = best_state
        global_best = (-1, ())
        for k in range(1, 5):
            score, tup = dp[n][k]
            if score > global_best[0] or (score == global_best[0] and tup < global_best[1]):
                global_best = (score, tup)
                
        return list(global_best[1])