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
Ohjelman testikattavuus kokonaisuudessaan on tällä hetkellä **93%**.

## Suorituskyky
Ohjelman suorituskykyä on testattu manuaalisesti erilaisilla syötteillä, kuten eri MIDI-tiedostoilla sekä eri sekvenssien pituuksilla, jota halutaan generoida.  
Esimerkiksi kun syötteeksi annetaan projektin juuressa oleva MIDI-tiedsoto *bad.mid* ja halutun sekvenssin pituudeksi 5000, niin ohjelman suorittamiseen menee noin 6.8 sekuntia, kun taas samalla sekvenssin pituudella 5000, mutta eri MIDI-tiedostolla *take-five.mid* aikaa kului 3.8 sekuntia. Tämä johtuu siitä, että *take-five.mid* sisältää 8 MIDI-raitaa, kun taas *bad.mid* sisältää 14 MIDI-raitaa. Eli toisin sanoen ohjelma joutuu generoimaan melkein puolet enemmän sekvenssejä, joka myös lisää ohjelman suoritusaikaa. 


## Suorituskykytaulukko
| MIDI-tiedosto  | Sekvenssin pituus | MIDI-raitoja | Suoritusaika (t:min:s.ms)
| ------------- | ------------- | ------------- |  ------------- |
| bad.mid  | 500  | 14  | 0:00:00.800000  |
| bb-king.mid  | 500  | 10  | 0:00:00.700000  |
| rick-astley.mid  | 500  | 16  | 000:00:01.000000  |
| take-five.mid  | 500  | 8  | 0:00:00.450000  |
| bad.mid  | 5000  | 14 | 0:00:06.840000  |
| bb-king.mid  | 5000  | 10 | 0:00:06.000000  |
| rick-astley.mid  | 5000  | 16  | 0:00:08.850000  |
| take-five.mid  | 5000 | 8 | 0:00:03.700000  |
| bad.mid  | 10 000  | 14 | 0:00:13.700000  |
| bb-king.mid  | 10 000  | 10 | 0:00:12.100000  |
| rick-astley.mid  | 10 000  | 16 | 0:00:18.350000  |
| take-five.mid  | 10 000  | 8 | 0:00:07.350000  |
| bad.mid  | 50 000  | 14  | 0:01:22.700000 |
| bb-king.mid  | 50 000  | 10 | 0:01:09.120000 |
| rick-astley.mid  | 50 000  | 16 | 0:01:45.850000 |
| take-five.mid  | 50 000  | 8 | 0:00:43.100000 |
