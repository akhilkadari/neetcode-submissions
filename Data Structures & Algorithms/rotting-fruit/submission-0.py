class Solution:
    """
    Approach 1
    Idea (BFS):
        1. First pass through the grid
            - count how many fresh fruits exist
            - collect all rotten fruits as starting points
        2. Treat all currently rotten fruits as the starting point for the BFS
        3. Process the BFS level by level
            - one BFS level -> one minute
            - when a rotten fruit touches a fresh neighbor, that fresh fruit becomes rotten 
            and gets added to the queue
        4. Continue until:
            - all fresh fruits are rotten, or queue becomes empty while fresh fruits still remain
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        fresh_count = 0
        queue = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0

        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        front = 0

        while front < len(queue) and fresh_count > 0:
            current_level_size = len(queue) - front

            for _ in range(current_level_size):
                row, col = queue[front]
                front += 1
                
                for row_offset, col_offset in directions:
                    next_row = row + row_offset
                    next_col = col + col_offset

                    if 0 <= next_row < rows and 0 <= next_col < cols:
                        if grid[next_row][next_col] == 1:
                            grid[next_row][next_col] = 2
                            fresh_count -= 1
                            queue.append((next_row, next_col))
            minutes += 1
        
        if fresh_count > 0:
            return -1

        return minutes




