class Solution:
    # def sortstr(self,s):
    #     s=s.split()
    #     s.sort()
    #     return ''.join(s)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict1 = defaultdict(list)
        
        for s in strs:
            key = ''.join(sorted(s))
            dict1[key].append(s)
            
        return list(dict1.values())