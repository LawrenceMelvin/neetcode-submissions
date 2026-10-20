from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
            group = defaultdict(list)
            #using sorted words as key
            # for word in strs:
            #     key = ''.join(sorted(word))

            #     group[key].append(word)

            # return list(group.values())

            

            for word in strs:
                count = [0] * 26
                for char in word:
                    index = ord(char) - ord('a')

                    count[index] += 1
                key = tuple(count)
                group[key].append(word)

            return list(group.values())


