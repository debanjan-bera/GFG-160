class Solution{
   void rotateArr(vector<int>& arr, int d) {
        // code here
        int n = arr.size();
        d %= n;
        rotate(arr,0,d-1);
        rotate(arr,d,n-1);
        rotate(arr,0,n-1);
    }
    void rotate(vector<int> &arr, int start, int end) {
        while (start < end) {
            int temp = arr[start];
            arr[start++] = arr[end];
            arr[end--] = temp;
        }
    }
};