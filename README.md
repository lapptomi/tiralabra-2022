# Aineopintojen harjoitustyö: Tietorakenteet ja algoritmit. 

### [Määrittelydokumentti](https://github.com/lapptomi/tiralabra-2022/blob/main/dokumentaatio/maarittelydokumentti.md)  
### [Viikkoraportit](https://github.com/lapptomi/tiralabra-2022/blob/main/dokumentaatio/viikkoraportit)
### [Testikattavuusraportti](https://lapptomi.github.io/tiralabra-2022/)

# Ohjelman suoritus
Ohjelman voi suorittaa antamalla komennon ``poetry run python3 src/index.py`` projektin juuressa.  
Tämän jälkeen projektin juurikansiion luodaan generoitu MIDI-tiedosto ``output.mid``, joka sisältää automaattisesti tuotetun musiikin, jonka voi toistaa erilaisilla DAW-ohjelmilla, tai verkossa esimerkiksi [Online Sequencerilla](https://onlinesequencer.net/import).

# Testaus
Testit voidaan suorittaa antamalla komennon ``poetry run pytest`` projektin juuressa.  

# Testikattavuus
Testikattavuuden voi tarkistaa antamalla komennon ``poetry run pytest --cov --cov-report=html:docs tests/`` projektin juuressa, jonka jälkeen testikattavuusraportti luodaan ``docs`` kansioon.  
