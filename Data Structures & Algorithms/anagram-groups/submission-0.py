class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmapdict={}
        for char in strs:
            sortedchar= sorted(char)
            finalchar= "".join(sortedchar)
            if finalchar not in  hashmapdict:
                hashmapdict[finalchar]=[]
            hashmapdict[finalchar].append(char)
        return list(hashmapdict.values())
        
        
            
