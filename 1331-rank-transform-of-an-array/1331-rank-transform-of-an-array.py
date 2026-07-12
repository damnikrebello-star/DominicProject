class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique_sorted = sorted(set(arr))
        rank_map ={val: index + 1 for index, val in enumerate(unique_sorted)}
        return [rank_map[num] for num in arr]