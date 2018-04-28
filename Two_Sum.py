class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        it1 = 0
        while target-nums[it1] not in nums or nums.index(target-nums[it1]) == it1:
            it1 += 1
        return [it1, nums.index(target-nums[it1])]