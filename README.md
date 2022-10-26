##  Aineopintojen harjoitustyö: Tietorakenteet ja algoritmit ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

### [Käyttöohje](https://github.com/lapptomi/tiralabra-2022/blob/main/dokumentaatio/käyttöohje.md)  
### [Suorituskyky / testausdokumentti](https://github.com/lapptomi/tiralabra-2022/blob/main/dokumentaatio/testausdokumentti.md)  
### [Toteutusdokumentti](https://github.com/lapptomi/tiralabra-2022/blob/main/dokumentaatio/toteutusdokumentti.md)  
### [Määrittelydokumentti](https://github.com/lapptomi/tiralabra-2022/blob/main/dokumentaatio/maarittelydokumentti.md)  
### [Viikkoraportit](https://github.com/lapptomi/tiralabra-2022/blob/main/dokumentaatio/viikkoraportit)

# Ohjelman suoritus
Ohjelman voi suorittaa antamalla komennon ``poetry run python3 src/index.py`` projektin juuressa.  
Tämän jälkeen projektin juurikansiion luodaan generoitu MIDI-tiedosto ``output.mid``, joka sisältää automaattisesti tuotetun musiikin, jonka voi toistaa erilaisilla DAW-ohjelmilla, tai verkossa esimerkiksi [Online Sequencerilla](https://onlinesequencer.net/import).

## Markov Chain Music Generator
Ohjelman tarkoituksena on tuottaa automaattisesti musiikkia Markovin ketjuja hyödyntäen. Ohjelmalle annetaan opetusdatana mikä tahansa MIDI-tiedosto, jonka jälkeen tätä tietoa käyttäen luodaan uusi MIDI-tiedosto ``output.mid``, joka sisältää generoidun musiikin.
