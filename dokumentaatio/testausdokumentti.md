# Testausdokumentti

## Testaus
Testit voidaan suorittaa antamalla komennon ``poetry run pytest`` projektin juuressa.  
Projektin testit on toteutettu Pytest-kirjastoa hyödyntäen.  

Yleisesti ohjelmassa on testattu lähes kaikkia funktioita, että ne palauttavat oikeat arvot.  
Trie-tietorakennetta on testattu siten, että lisätessä bigrammeja tarkistetaan lopuksi, 
että Trien search-funktio palauttaa oikean määrän bigrammeja. Myös Trien insert on testattu palauttavan oikean määrän bigrammeja.  

Musiikin automaattista luomista on testattu mm. siten, että aluksi generoidaan jokaiselle MIDI-raidalle omat sekvenssit, 
jotka tallennetaan Python dictionaryyn, jonka jälkeen nämä sekvenssit kirjoitetaan MIDI-tiedostoon, joka kirjoitetaan tiedostoon *"output.md"*.  
Tämän jälkeen testit hakevat luodun MIDI-tiedoston datan jokaiselta raidalta ja tarkistaa, että ne vastaavat pituudeltaan, sekä sisällöltään 
aiemmin generoituja sekvenssejä.

## Testikattavuus
### [Testikattavuusraportti](https://lapptomi.github.io/tiralabra-2022/)  
Testikattavuusraportin voi luoda antamalla komennon ``poetry run pytest --cov --cov-report=html:docs tests/`` projektin juuressa, 
jonka jälkeen testikattavuusraportti luodaan ``docs`` kansioon.  
Ohjelman testikattavuus kokonaisuudessaan on tällä hetkellä **94%**.