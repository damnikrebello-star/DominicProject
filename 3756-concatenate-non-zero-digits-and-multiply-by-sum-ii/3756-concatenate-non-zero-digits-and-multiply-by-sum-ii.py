import bisect
from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        indices = []
        digits = []
        
        for i, char in enumerate(s):
            if char != '0':
                indices.append(i)
                digits.append(int(char))
                
        k = len(digits)
        

        pref_sum = [0] * (k + 1)
        for i in range(k):
            pref_sum[i + 1] = pref_sum[i] + digits[i]

        P = [0] * (k + 1)
        for i in range(k):
            P[i + 1] = (P[i] * 10 + digits[i]) % MOD

        pow10 = [1] * (k + 1)
        for i in range(1, k + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        ans = []

        for l, r in queries:

            left_idx = bisect.bisect_left(indices, l)
            right_idx = bisect.bisect_right(indices, r) - 1
            
            if left_idx > right_idx:

                ans.append(0)
            else:
                length = right_idx - left_idx + 1

                x = (P[right_idx + 1] - P[left_idx] * pow10[length]) % MOD

                digit_sum = pref_sum[right_idx + 1] - pref_sum[left_idx]

                ans.append((x * digit_sum) % MOD)
                
        return ans