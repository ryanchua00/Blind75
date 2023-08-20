from typing import List, Dict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # go through strings
        # make a dictionary of each string
        # for dictionaries that already exist, add to list
        groupAnagrams: Dict[str, List[str]] = {}
        for str in strs:
            sorted_string = ''.join(sorted(str))
            list = groupAnagrams.get(sorted_string, [])
            list.append(str)
            groupAnagrams[sorted_string] = list
        return groupAnagrams.values()