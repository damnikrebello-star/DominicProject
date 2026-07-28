class Solution:
    def smallestPalindrome(self, s: str) -> str:

        char_counts = [0] * 26
        for char in s:
            char_counts[ord(char) - ord('a')] += 1
            
        first_half = []
        mid = ""

        for i in range(26):
            if char_counts[i] > 0:
                char = chr(i + ord('a'))

                first_half.append(char * (char_counts[i] // 2))
                

                if char_counts[i] % 2 == 1:
                    mid = char

        first_half_str = "".join(first_half)

        return first_half_str + mid + first_half_str[::-1]