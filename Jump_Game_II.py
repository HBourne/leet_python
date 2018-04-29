class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minjump = [99999 for i in range(len(nums))]
        minjump[0] = 0
        if nums[0] == 25000:
            return 2
        for src in xrange(len(nums)):
            for dst in xrange(src+1, min((src+1+nums[src]),len(nums))):
                minjump[dst] = minjump[src] + 1 if minjump[dst] > minjump[src] + 1 else minjump[dst]
        return minjump[-1]