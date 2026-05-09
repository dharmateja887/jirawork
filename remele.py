class Solution:
    def removeelement(self,nums,val):
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k
a=Solution()
nums1=[3,2,2,3]
val1=3
k1=a.removeelement(nums1,val1)
print("no of elements:",k1)
print("updated:",nums1[:k1]) 
nums2=[0,1,2,2,3,0,4,2]
val2=2
k2=a.removeelement(nums2,val2)
print("no of elements:",k2)
print("updated:",nums2[:k2])