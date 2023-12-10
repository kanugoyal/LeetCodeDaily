from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        col = 0
        
        while col < len(matrix[0]):
            temp = []
            
            for i in range(len(matrix)):
                temp.append(matrix[i][col])
            
            ans.append(temp)
            col += 1
        
        return ans

        