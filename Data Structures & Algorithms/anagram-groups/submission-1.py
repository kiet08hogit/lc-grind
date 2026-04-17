class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicttemp = {}
        for word in strs:
            sortedchar= sorted(word)
            finalword= "".join(sortedchar)
            if finalword not in dicttemp:
                dicttemp[finalword]=[]
            dicttemp[finalword].append(word)
        return list(dicttemp.values())
        
        
            
