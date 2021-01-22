#Array Partition I 561 Easy

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_a = sorted(nums)
        return sum(sorted_a[::2])
        
