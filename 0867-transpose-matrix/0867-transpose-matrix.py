class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        transpose = []
        for i in range(cols):
            row = []
            for j in range(rows):
                row.append(matrix[j][i])
            transpose.append(row)
        return transpose