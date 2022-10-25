#  Käyttöohje  

## Ohjelman suoritus
Ohjelman voi suorittaa antamalla komennon ``poetry run python3 src/index.py`` projektin juuressa. *Huom. Käyttäjällä tulee olla Poetry asennettuna, jotta ohjelman suoritus on mahdollista*. Ohjelmaa suorittaessa aluksi käyttäjältä kysytään MIDI-tiedoston nimeä, jota halutaan käyttää opetusdatana musiikin tuottamiseen, kuten esimerkiksi projektin juuressa valmiina olevat MIDI-tiedostot "bad.mid" tai "bb-king.mid".  
Käyttäjä voi myös itse käyttää haluamiaan MIDI-tiedostoja opetusdatana, mutta tiedostot tulee sijoittaa projektin juureen, jotta ohjelma osaa lukea niitä.  
Tämän jälkeen Käyttäjältä kysytään sekvenssin pituutta, joka halutaan luoda. Tämä voi olla esimerkiksi 30-200.  

Kun käyttäjä on antanut MIDI-tiedoston nimen sekä sekvenssin pituuden, luo ohjelma projektin juureen uuden MIDI-tiedoston *output.mid*, joka sisältää automaattisesti tuotetun musiikin.  
Kyseisen MIDI-tiedoston voi toistaa erilaisilla DAW-ohjelmilla, tai helposti verkossa esimerkiksi [Online Sequencerilla](https://onlinesequencer.net/import). 
