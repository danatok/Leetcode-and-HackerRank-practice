class SparseVector:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.array = nums
​  def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        result = 0
        for i, j in zip(self.array, vec.array):
            result += i * j
        return result