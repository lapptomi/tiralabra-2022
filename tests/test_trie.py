from src.Trie import trie

T = trie.Trie()

sequence = ['C4', 'C4', 'E4', 'G4', 'A♯3', 'G1', 'C♯3', 'C4', 'E4', 'G4']

def insert_bigrams():
    # Insert MIDI notes into Trie data structure as bigrams
    for i in range(len(sequence)-1):
        T.insert(sequence[i]+'-'+sequence[i+1])

def test_trie_insert():
    insert_bigrams()
    assert len(T.search('')) == 7

def test_trie_search():
    insert_bigrams()

    assert len(T.search('')) == 7
    assert len(T.search('C')) == 3
    assert len(T.search('C4-C4')) == 1
    assert len(T.search('C♯')) == 1
    assert len(T.search('C♯3-C4')) == 1
    