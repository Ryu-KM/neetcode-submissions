class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # get the length of the list
        listLength = len(nums)
        # convert the list into a set
        newSet = set(nums)
        # check if there are any repetitions in the list 
        return listLength != len(newSet)