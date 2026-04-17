class Solution:
    def helperdict(self, tempdict: dict, word: str):
        for ch in word:
            tempdict[ch] = tempdict.get(ch, 0) + 1

    def checkInclusion(self, s1: str, s2: str) -> bool:
  
        tempdict1 = {}
        self.helperdict(tempdict1, s1)

        window_size = len(s1)

        l = 0
        r = window_size - 1

        while r < len(s2):
            tempdict2 = {}
            self.helperdict(tempdict2, s2[l:r+1])

            if tempdict1 == tempdict2:
                return True

            l += 1
            r += 1

        return False
