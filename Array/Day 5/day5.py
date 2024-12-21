class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        pivot = -1
        for i in range(n - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                pivot = i
                break
        else:
            arr.reverse()
            return
        
        for i in range(n - 1, pivot, -1):
            if arr[pivot] < arr[i]:
                arr[i], arr[pivot] = arr[pivot], arr[i]
                break
        pivot += 1
        n -= 1
        while pivot < n:
            arr[pivot], arr[n] = arr[n], arr[pivot]
            pivot += 1
            n -= 1