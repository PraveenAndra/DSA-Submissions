class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorting
        # lookup = defaultdict(list)
        # for i in strs:
        #     s = "".join(sorted(i))
        #     lookup[s].append(i)
        # return list(lookup.values())
        
        lookup = defaultdict(list)
        for i in strs:
            l = [0]*26
            for j in i:
                l[ord(j) - ord('a')] += 1
            lookup[tuple(l)].append(i)
        return list(lookup.values())