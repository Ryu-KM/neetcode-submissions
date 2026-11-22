class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash = {}

        for key,num_value in enumerate(nums):
            comp = target - num_value
            if comp in num_hash:
                return [num_hash[comp],key]
            num_hash[num_value] = key
