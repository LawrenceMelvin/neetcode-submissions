class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #set can contain only unique numbers
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False