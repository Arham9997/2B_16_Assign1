#User function Template for python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
		rev_s=s[::-1]
		if(rev_s==s):
		    return True
		else:
		    return False