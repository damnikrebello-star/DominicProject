class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        n = len(nums)

        sorted_nums = sorted([(num, i) for i, num in enumerate(nums)])
        
        result = [0] * n
        i = 0
        
        while i < n:
            j = i + 1

            while j < n and sorted_nums[j][0] - sorted_nums[j-1][0] <= limit:
                j += 1

            indices = sorted([sorted_nums[k][1] for k in range(i, j)])

            for k in range(i, j):
                result[indices[k-i]] = sorted_nums[k][0]

            i = j
            
        return result