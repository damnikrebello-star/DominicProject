class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        u =set(nums)

        s1 = u

        s2 = {x ^ y for x in s1 for y in u}

        s3 = {x ^ y for x in s2 for y in u}

        return len(s3)