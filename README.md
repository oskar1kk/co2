# CO₂ Monitorings

Vienkārša tīmekļa aplikācija CO₂ līmeņa datu skatīšanai un analīzei telpā.

## Par projektu

Projekts paredzēts CO₂ mērījumu datu vizualizācijai. Dati tiek glabāti CSV failā un attēloti divos veidos - grafiskā un tabulas formātā. Aplikācija rakstīta ar Flask. Funkcijas: datu attēlošana līniju grafikā, datu filtrēšana pēc dienas, gaisa kvalitātes krāsu kodējums, statistika par mērījumiem.

## Instalācija

Lai uzstādītu programmu, vispirms klonējiet repozitoriju vai lejupielādējiet visus failus kā ZIP arhīvu. Komandrindā ierakstiet: git clone https://github.com/lietotajs/co2-monitorings.git un cd co2-monitorings. Pēc tam uzstādiet Flask, izmantojot komandu pip install flask. Visbeidzot palaidiet aplikāciju ar python co2.py un atveriet pārlūkā adresi http://localhost:5000.

## Galvenie faili

Projektā ir šādi galvenie faili: co2.py - Flask serveris, kas apstrādā pieprasījumus; CO2.csv - fails ar CO₂ mērījumu datiem; templates/start.html - sākuma lapa ar izvēlni; templates/graph.html - lapa ar grafiku; templates/data.html - lapa ar tabulu un filtriem. Visiem HTML failiem jāatrodas mapē templates.

## Kā lietot programmu

Datu ievadīšanai jālabo CO2.csv fails. Faila struktūra ir šāda: pirmajā kolonnā ir mērījuma numurs, otrajā - CO₂ līmenis ppm, trešajā - dienas numurs. Piemēram: "1",1245.67,1. Pievienojot jaunus datus, vienkārši ierakstiet jaunu rindu faila beigās.

Lietošanas piemēri. Lai apskatītu CO₂ līmeni konkrētā dienā, atveriet Datu skatu, izvēlieties dienu no saraksta un nospiediet "Pielietot Filtru". Lai redzētu visus datus uzreiz, nospiediet "Rādīt Visu Informāciju". Grafika skatā punkti uz līnijas ir iekrāsoti atbilstoši gaisa kvalitātei: zaļš nozīmē labu gaisu (zem 1000 ppm), oranžs - vidēju (1000-2000 ppm), sarkans - sliktu (virs 2000 ppm). Uzbradot ar peli virs punkta, parādās precīza vērtība. Tabulā datus var kārtot, noklikšķinot uz kolonnas virsraksta.

Gaisa kvalitātes skala: 420 ppm ir svaiga gaisa bāzes līmenis, 420-1000 ppm - labs gaiss, 1000-2000 ppm - gaiss pasliktinās, 2000-3000 ppm - būtiski sliktāks, 3000-5000 ppm - veselībai bīstami, virs 5000 ppm - bīstams.

## Licence

Šis projekts ir licencēts saskaņā ar MIT licenci. Tas nozīmē, ka ikviens, kas saņem šīs programmatūras kopiju, var bez maksas to izmantot, mainīt, apvienot, publicēt un izplatīt. Pilns licences teksts: MIT License, Copyright (c) 2024.
