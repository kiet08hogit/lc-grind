class Solution:

    def encode(self, strs: List[str]) -> str:
        self.words= strs
        self.sentence= ",".join(strs)
        return self.sentence
    def decode(self, s: str) -> List[str]:
        return self.words
       