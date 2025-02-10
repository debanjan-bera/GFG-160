class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        #Your code here
        arr.sort()
        l, r, ans = 0, len(arr) - 1,0
        while l< r:
            if arr[l] + arr[r] < target: ans += (r - l); l+=1
            else: r -= 1
        return ans