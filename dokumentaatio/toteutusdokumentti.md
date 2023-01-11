# Toteutusdokumentti  

## Ohjelman yleisrakenne
Ohjelman toiminnallisuus on pääasiassa toteutettu tiedostoon *index.py*, mutta Trie-tietorakenne on luotu kansioon Trie. Trie on toteutettu kahteen eri tiedostoon *trie.py* sekä *trie_node.py*. *Trie.py* sisältää tietorakenteen yleisen toiminnallisuuden ja *trie_node.py* nimensä mukaisesti toimii Trien solmuna, jota hyödynnetään tiedostossa *trie.py*.

## Saavutetut aika- ja tilavaativuudet 
### Aikavaativuus
Ohjelma kokonaisuudessaan toimii ajassa *O(n^3)*, sillä generoidessa sekvennsit jokaiselle MIDI-raidalle vie hieman enemmän aikaa, kuin esimerkiksi vain yhdelle raidalle.

## Työn mahdolliset puutteet ja parannusehdotukset  
Tällä hetkellä ohjelma lukee vain käytetyt nuotit opetusdatana käytettävän MIDI-tiedoston jokaiselta raidalta, jota käytetään sekvennsien generoimiseen, mutta yksi parannusehdotus olisi esimerkiksi hyödyntää myös MIDI-tiedoston käytettyjen nuottien kestoa sekä äänenvoimakkuutta. Tämä kuitenkin lisäisi työn vaativuutta paljon, joten tällä hetkellä näihin liittyen luodaan vain satunnaiset muuttujat Pythonin *randrange*-funktiota hyödyntäen MIDI-tiedostoa luodessa, jotta saadaan hieman vaihtelevuutta luotuun musiikkiin.

## Lähteet
https://www.geeksforgeeks.org/trie-insert-and-search/  
