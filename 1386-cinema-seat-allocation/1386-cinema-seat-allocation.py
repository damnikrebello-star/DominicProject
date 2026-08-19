class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = collections.defaultdict(set)
        for row, seat in reservedSeats:
            if seat in (2, 3, 4, 5, 6, 7, 8, 9):
                seats[row].add(seat)
        
        res = (n - len(seats)) * 2
        
        for row, reserved in seats.items():
            left = not (reserved & {2, 3, 4, 5})
            right = not (reserved & {6, 7, 8, 9})
            
            if left and right:
                res += 2
            elif left or right:
                res += 1
            elif not (reserved & {4, 5, 6, 7}):
                res += 1
                
        return res