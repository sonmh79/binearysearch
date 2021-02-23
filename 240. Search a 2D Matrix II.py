class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 최초의 풀이, 순서대로 탐색
        '''
        for i in range(len(matrix)):
            b= bisect.bisect_left(matrix[i],target)
            for j in range(b,len(matrix[0])):
                if matrix[i][j] == target:
                    return True
                    '''
        # 첫 행의 맨 끝부터 탐색
        '''
        if not matrix:
            return False
        row,col = 0, len(matrix[0])-1
        while row <=len(matrix)-1 and col >=0:
            if matrix[row][col] > target:
                col -=1
            elif matrix[row][col] < target:
                row +=1
            else:
                return True
        return False
        '''
        # 파이썬 다운 방식
        return any(target in row for row in matrix)
