class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        # base case 
        if self.is_inbounds(grid, row, col):
	     # transform land into water so we don't revisit this cell.
            grid[row][col] = "L"
 
            for new_row, new_col in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                self.dfs(new_row, new_col, grid)
 
   # validation: row and col are within the grid and the cell is a land.
    def is_inbounds(self, grid: list[list[str]], row: int, col: int) -> bool:
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == "W"
    
    def numIslands(self, grid: list[list[str]]) -> int:
        count = 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        
        for row in range(0, num_rows):
            for col in range(0, num_cols):
                if grid[row][col] == "W":
                    count += 1
                    self.dfs(row, col, grid)
                    
        print (count)
    

