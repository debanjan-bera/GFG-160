#include <bits/stdc++.h> // For string, vector, and reverse
using namespace std;

class Solution {
public:
    int computelps(string c) {
        int n = c.size();
        int l = 0, i = 1;
        vector<int> lps(n, 0); // Initialize LPS array
        
        while (i < n) {
            if (c[i] == c[l]) {
                l++;
                lps[i] = l; // Corrected to store the length of the prefix match
                i++;
            } else {
                if (l != 0) {
                    l = lps[l - 1]; // Use previous prefix match
                } else {
                    lps[i] = 0; // No prefix match
                    i++;
                }
            }
        }
        
        return lps[n - 1]; // Return the last value of the LPS array
    }

    int minChar(string& s) {
        // Compute the minimum characters to add to make a palindrome
        string t = s;
        reverse(t.begin(), t.end());
        return s.size() - computelps(s + "#" + t);
    }
};
