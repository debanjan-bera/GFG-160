
class Solution {
    public int maximumProfit(int prices[]) {
        // Code here
        int res = 0, min = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[min])
                res = Math.max(res, prices[i] - prices[min]);
            else
                min = i;
        }
    
        return res;
    }
}