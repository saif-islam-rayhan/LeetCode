class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0

        for i in range(len(nums)):
            count=0
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    count=count+1

            ans+=count
        return ans     
