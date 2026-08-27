from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        total_counts = Counter(s)
        
        def get_rem_counts(prefix_len):
            rem = total_counts.copy()
            for ch in target[:prefix_len]:
                if rem[ch] == 0:
                    return None
                rem[ch] -= 1
            return rem

        for L in range(n, -1, -1):
            rem = get_rem_counts(L)
            if rem is None:
                continue

            if L == n:
                continue

            t_char = target[L]
            

            best_char = None
            for ch in sorted(rem.keys()):
                if ch > t_char and rem[ch] > 0:
                    best_char = ch
                    break
            
            if best_char:
                rem[best_char] -= 1

                tail = []
                for ch in sorted(rem.keys()):
                    tail.append(ch * rem[ch])
                
                return target[:L] + best_char + "".join(tail)
                
        return ""