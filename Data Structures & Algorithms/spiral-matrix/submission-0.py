class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result=[]
        top=0
        bottom=len(matrix)-1
        right=len(matrix[0])-1
        left=0

        while top<=bottom and left<=right:
            for c in range(left,right+1):
                result.append(matrix[top][c])
            top+=1

            for r in range(top,bottom+1):
                result.append(matrix[r][right])
            right-=1
            if top<=bottom:
                for c in range(right,left-1,-1):
                    result.append(matrix[bottom][c])
                bottom-=1
            if left<=right:
                for r in range(bottom,top-1,-1):
                    result.append(matrix[r][left])
                left+=1
        return result