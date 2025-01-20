from collections import defaultdict
class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        umap = defaultdict(list)
        for s in arr:
            sorted_s = ''.join(sorted(s))
            umap[sorted_s].append(s)
        return list(umap.values())