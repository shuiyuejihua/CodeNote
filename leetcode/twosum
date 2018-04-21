class Solution:
    def twosum(self,nums,target):
        """
	:type nums:List[list]
	:type target:int
	:rtype List[int]
	"""
	d = {}
	for i,n in enumerate(nums):
	    m = target - n
	    if m in d:
	        return [d[m],i]
	    else:
	        d[n] = i
