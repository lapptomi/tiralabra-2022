from src.Trie import trie

T = trie.Trie()

seq = ['C4', 'C4', 'E4', 'G4', 'A♯3', 'G1', 'C♯3', 'C4', 'E4', 'G4']

def test_trie():
    # Insert MIDI notes into Trie data structure as bigrams
    for i in range(len(seq)-1):
        T.insert(seq[i]+'-'+seq[i+1])


    assert len(T.search('')) == 7
    assert len(T.search('C')) == 3
    assert len(T.search('C♯')) == 1