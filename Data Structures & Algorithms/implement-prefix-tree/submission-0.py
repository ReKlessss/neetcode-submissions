class TrieNode:
    def __init__(self, val, ending_letter: bool = False):
        self.val = val
        self.children = [None] * 26
        self.isEndOfWord = ending_letter


class PrefixTree:

    def __init__(self):
        self.root = TrieNode("ROOT")

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            i = ord(c) - ord("a")
            if not curr.children[i]:
                curr.children[i] = TrieNode(c)
            
            curr = curr.children[i]

        curr.isEndOfWord = True


    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            i = ord(c) - ord("a")
            if not curr.children[i]:
                return False
            
            curr = curr.children[i]

        return curr.isEndOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            i = ord(c) - ord("a")
            if not curr.children[i]:
                return False

            curr = curr.children[i]

        return True
        
        