class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        total_elements = m * n
        

        k = k % total_elements 
        if k == 0:
            return grid

        res = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):

                flat_index = i * n + j

                new_flat_index = (flat_index + k) % total_elements
                
                new_i = new_flat_index // n
                new_j = new_flat_index % n

                res[new_i][new_j] = grid[i][j]
                
        return res