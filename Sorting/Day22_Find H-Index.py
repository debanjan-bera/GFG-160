class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        #code here
        n = len(citations)
        buckets = [0] * (n + 1)

        for c in citations:
            if c >= n:
                buckets[n] += 1
            else:
                buckets[c] += 1

        cumulative = 0
        for i in range(n, -1, -1):
            cumulative += buckets[i]
            if cumulative >= i:
                return i
        return 0
