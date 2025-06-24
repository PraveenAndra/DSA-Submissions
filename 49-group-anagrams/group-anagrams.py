class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorting
        lookup = defaultdict(list)
        for i in strs:
            s = "".join(sorted(i))
            lookup[s].append(i)
        return list(lookup.values())
        