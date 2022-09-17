class TrieNode:
    def __init__(self, note):
        self.note = note
        self.end = False
        self.counter = 0
        self.children = {}