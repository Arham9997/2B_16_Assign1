class Solution:
    def getSecondLargest(self, arr):
        s=set(arr)
        l=list(s)
        if len(l)<2:
            return -1
        l.sort()
        for i in l:
            if len(l)>1:
                return l[-2]