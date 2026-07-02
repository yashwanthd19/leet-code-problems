from typing import List
from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        min_cost = [[float('inf')] * n for _ in range(m)]
        queue = deque([(0, 0)])
        min_cost[0][0] = grid[0][0]
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c = queue.popleft()
            if r == m - 1 and c == n - 1:
                break
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    cost = grid[nr][nc]
        
                    if min_cost[r][c] + cost < min_cost[nr][nc]:
                        min_cost[nr][nc] = min_cost[r][c] + cost
                        
                    
                        if cost == 0:
                            queue.appendleft((nr, nc))
                        else:
                            queue.append((nr, nc))
                            

        return min_cost[m - 1][n - 1] < health
from typing import List
from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        

        min_cost = [[float('inf')] * n for _ in range(m)]
        queue = deque([(0, 0)])
        min_cost[0][0] = grid[0][0]
        
    
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c = queue.popleft()
        
            if r == m - 1 and c == n - 1:
                break
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                

                if 0 <= nr < m and 0 <= nc < n:
                    cost = grid[nr][nc]
                 
                    if min_cost[r][c] + cost < min_cost[nr][nc]:
                        min_cost[nr][nc] = min_cost[r][c] + cost
                        
                  
                        if cost == 0:
                            queue.appendleft((nr, nc))
                        else:
                            queue.append((nr, nc))
         
        return min_cost[m - 1][n - 1] < health

        