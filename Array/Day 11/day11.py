class Solution:
    # Function to find the maximum product subarray
    def maxProduct(self, arr):
        # code here
        n = len(arr)
        res = arr[0]
        maxLeft = maxRight = 1
        
        for i in range(n):
            # Reset maxLeft if it becomes 0
            if maxLeft == 0:
                maxLeft = 1
            # Reset maxRight if it becomes 0
            if maxRight == 0:
                maxRight = 1
            
            j = n - i - 1
            maxLeft *= arr[i]
            maxRight *= arr[j]
            res = max(maxLeft, maxRight, res)
        
        return res
