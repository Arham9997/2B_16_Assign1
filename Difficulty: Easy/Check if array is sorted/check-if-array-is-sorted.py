class Solution:
    def isSorted(self, arr) -> bool:
        n=len(arr)
        for i in range(n-1):
            if arr[i]>arr[i + 1]:
                return False  
        return True
c1=Solution()
c1.isSorted([1,2,3,4,5])