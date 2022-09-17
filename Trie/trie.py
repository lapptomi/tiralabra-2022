from Trie.trie_node import TrieNode


class Trie(object):
    def __init__(self):
        self.root = TrieNode('')
        
    def dfs(self, node, prefix):
        if node.end:
            self.output.append((prefix + node.note, node.counter))
        
        for child in node.children.values():
            self.dfs(child, prefix + node.note)

    def insert(self, sequence):
        node = self.root
        
        for char in sequence:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        
        node.end = True
        node.counter += 1
        
    def search(self, x):
        self.output = []
        node = self.root
        
        for note in x:
            if note in node.children:
                node = node.children[note]
            else:
                return []
        
        self.dfs(node, x[:-1])

        return sorted(self.output, key=lambda x: x[1], reverse=True)