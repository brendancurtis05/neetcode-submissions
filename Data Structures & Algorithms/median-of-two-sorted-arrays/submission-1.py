class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2 #assign array 1 and 2
        total = len(A) + len(B)
        half = total//2

        if len(B) < len(A): #we want to binary search on the smaller array (A)
            A, B = B, A

        l,r = 0, len(A)-1
        while True: #we are garunteed a median
            i = (l+r)//2 #middle for A
            j = half - i - 2 #middle for B (subract 2 because A starts at index 0 and B starts at 0)

            Aleft = A[i] if i >=0 else float("-infinity") #if index out of bounds edge cases
            Aright = A[i+1] if (i+1) < len(A) else float("infinity")
            Bleft = B[j] if j >=0 else float("-infinity") 
            Bright = B[j+1] if (j+1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                #odd num of elements
                if total % 2 == 1:
                    return min(Aright,Bright)
                #even
                return ((max(Aleft,Bleft) + min(Aright,Bright)) / 2)

            elif Aleft > Bright: #too many elements in A
                r = i-1
            else: #too few elements in A
                l = i+1
