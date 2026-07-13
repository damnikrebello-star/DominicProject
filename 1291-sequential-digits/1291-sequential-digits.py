class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample = "123456789"
        result = []

        for length in range(2, 10):
            for i in range(10 - length):
                num = int(sample[i:i + length])

                if low <= num <= high:
                    result.append(num)
                    
        return result