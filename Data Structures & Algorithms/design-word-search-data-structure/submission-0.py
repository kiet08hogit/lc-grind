

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr= self.root
        for char in word:
            if char not in curr.children:
                curr.children[char]= TrieNode()
            curr = curr.children[char]
        curr.is_end = True
    def search(self, word: str) -> bool:
        def dfs(index,curr):
            if index == len(word):
                return curr.is_end
            temp = word[index]
            if temp == '.':
                for child in curr.children.values():
                    if dfs(index+1,child):
                        return True
            if temp not in curr.children:
                return False
            return dfs(index+1,curr.children[temp])
        return dfs(0,self.root)