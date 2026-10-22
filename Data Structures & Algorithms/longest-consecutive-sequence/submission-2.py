
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        max_count = 0

        for i in range(len(nums)):
            count = 1

            if nums[i] - 1 not in res:
                start_seq = nums[i]

                while start_seq + 1 in res:
                    count += 1
                    start_seq += 1

                max_count = max(count, max_count)

        return max_count
