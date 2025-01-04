class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        # code here
        result = []
        top,left,bottom,right = 0,0, len(mat) - 1, len(mat[0]) - 1
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                result.append(mat[top][i])
            top += 1
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -=1
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(mat[bottom][i])
                bottom -=1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left +=1
                
        return result