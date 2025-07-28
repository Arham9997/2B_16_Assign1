#User function Template for python3

class Solution:
    def reverseString(self, s: str) -> str:
        rev_s=""
        for char in s:
            rev_s=char+rev_s
        return rev_s
