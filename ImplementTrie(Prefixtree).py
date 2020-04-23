class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cursor = self.root
        for s in range(len(word)):
            if cursor.children[ord(word[s]) - ord('a')] is None:
                cursor.children[ord(word[s]) - ord('a')] = TrieNode()
            cursor = cursor.children[ord(word[s]) - ord('a')]
        # After traversing through entire word
        cursor.isEndOfWord = True
                
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cursor = self.root
        for i in range(len(word)):
            if cursor.children[ord(word[i]) - ord('a')] == None:
                return False
            cursor = cursor.children[ord(word[i]) - ord('a')]
        return cursor.isEndOfWord   
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cursor = self.root
        for i in range(len(prefix)):
            if cursor.children[ord(prefix[i]) - ord('a')] == None:
                return False
            cursor = cursor.children[ord(prefix[i]) - ord('a')]
        return True
    

class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.isEndOfWord = False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)