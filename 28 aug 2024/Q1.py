# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
# ![alt text](Q1.py)        
        


from typing import List
nums =[1,2,3,4,5,6,7]
k = 4
# [3,99,-1,-100]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums[:]=nums[k+1:]+nums[:k+1]
        nums[:]=nums[-k:]+nums[:-k]
        print(nums)


Solution().rotate(nums,k)
print()











































# numss=[]
# n=[]

# # [5,6,7,1,2,3,4]

# def rotate():
#     x=len(nums)-k
#     y=nums[::-1]
 
#     for i in range(k):
#        z=y[i]
#        n.append(z)
#     b=n[::-1]   
#     for i in range(k):
#         numss.append(b[i])
#     for i in range(x):
#         numss.append(nums[i])       
 
#     print(numss)   
    
        
    
        
# rotate()       

