class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchRowMatrix(self, mat, x): 
    	# code here 
    	for row in mat:
    	    if x in row:
    	        return True
    	return False