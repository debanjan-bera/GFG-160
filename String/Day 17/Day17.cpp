class Solution {
  public:
    // Function to find the first non-repeating character in a string.
    char nonRepeatingChar(string &s) {
        // Your code here
        unordered_map<char, int> chCount;
        for (char ch : s) {
           if (chCount[ch])
                chCount[ch] += 1;
            else
                chCount[ch] = 1;
        }
        for (char ch : s) {
            if (chCount[ch] == 1)
                return ch;
        }
        return '$';
    }
};