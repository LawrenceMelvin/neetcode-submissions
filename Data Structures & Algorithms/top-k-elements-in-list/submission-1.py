
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        result = []

        for key, val in sorted(c.items(), key=lambda x: x[1], reverse=True):
            result.append(key)
            if len(result) == k:
                break

        return result
