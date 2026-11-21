class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # start loop need to have a nested loop i needs to point to the first element and j needs to start at the second, once we 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    #return ouput
                    return [i,j]