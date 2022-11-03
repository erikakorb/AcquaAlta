Python script per visualizzare in tempo reale l'evoluzione della marea e il fenomeno dell'acqua alta nella laguna di Venezia

# Il fenomeno dell'acqua alta
 L'altezza della marea nei centri storici di Venezia e Chioggia è determinata principalmente da due fattori: la marea astronomica e il vento. La marea astronomica determina il livello medio dell'acqua, alternando massimi e minimi ogni 6 ore circa. Il vento forte, quando presente, spinge una quantità maggiore di acqua dentro la laguna di Venezia e fa innalzare la marea. La direzione del vento determina il lato della laguna dove la marea si alza di più: lo scirocco spinge l'acqua verso Venezia, la bora verso Chioggia. 
 
## L'acqua granda del 12 novembre 2019
 Il [12 novembre 2019](http://www.ismar.cnr.it/file/news-e-eventi/Acqua_Granda_2019_v03.pdf ) la marea in centro storico a Venezia ha toccato i 187 cm sul livello del mare (rilevatore di Punta Salute). La marea è stata così alta perché i venti di 100 km/h (e raffiche di 110 km/h, come rilevato dalla piattaforma Acqua Alta in Adriatico) provenienti da sud-ovest ed un accentuato minimo barico locale si sono verificati in corrispondenza del picco della marea astronomica. 
 
 L' evento del 12 novembre è stato eccezionale ma si è inserito in una settimana di acque alte eccezionali. Ricordando che [il piano calpestabile di Venezia si trova indicativamente a 100 cm sul medio mare](http://smu.insula.it/index.php@option=com_content&view=article&id=114&Itemid=81&lang=it.html), in 6 giorni vi sono stati 8 picchi di marea superiori ai 100 cm e 4 di essi hanno superato anche i 140 cm (eventi eccezionali).
 
 ![plot](./archivio/2019-11-12/storico.png) 
 
## Il MOSE
Per evitare eventi eccezionali e settimane come quella del 12 novembre 2019, il [3 ottobre 2020](https://www.mosevenezia.eu/prima-prova-del-mose-contro-lacqua-alta/ ) è entrato in funzione il sistema di paratie mobili MOSE. Da allora e sebbene ancora incompleto, il MOSE è stato azionato più volte per evitare che maree superiori ai 110 cm potessero verificarsi a Venezia. Le paratie del MOSE impediscono all'acqua del mare di entrare nella laguna di Venezia: il surplus di acqua accumulata per effetto del vento rimane confinato nell'Adriatico e la marea in laguna viene mantenuta all'incirca costante. 

### MOSE attivo
Ad esempio, il 15 ottobre 2020 il MOSE è entrato in funzione per la seconda volta evitando un'altra potenziale marea eccezionale. I venti di 60 km/h provenienti da nord/nord-ovest hanno causato una marea di 130-140 cm nelle bocche di porto mentre la marea in laguna è rimasta stabile attorno ai 70 cm, con una differenza di circa 20 cm tra Venezia e Chioggia a causa dello spostamento d'acqua comunque presente all'interno della laguna stessa.

 ![plot](./archivio/2020-10-15/15ott2020_marea_finale.png) 
 
### MOSE non attivo
L'8 dicembre 2020 il MOSE non è stato attivato e la marea è stata eccezionale. Il forte vento ha impedito alla marea di defluire fuori dalla laguna e ha causato un minimo mareale di fatto coincidente con il picco precedente. Pertanto, il picco successivo ha avuto una base di partenza eccezionalmente alta e la continua azione del vento ha permesso di accumulare altra acqua in laguna. Senza le paratie del MOSE, a Venezia e Chioggia la marea ha raggiunto il livello osservato nelle bocche di porto. In entrambe le città, la marea ha seguito l'andamento delle bocche di porto, pur manifestando un ritardo di un'ora a causa della distanza che separa i due centri storici dagli sbocchi sull'Adriatico.

 ![plot](./archivio/2020-12-08/8dic2020_marea.png) 

# Lo script Python
Il Python script **acqua_alta.py** scarica e visualizza in tempo reale i dati raccolti nelle 24 ore precedenti da alcune delle [stazioni meteorologiche usate dal Centro Maree del Comune di Venezia](https://www.comune.venezia.it/content/dati-dalle-stazioni-rilevamento). Di default il programma analizza i dati sull'altezza della marea, velocità e direzione del vento dalle seguenti stazioni (tra parentesi è indicato il nome usato nei grafici):
- `Punta Salute` (Venezia), come riferimento per la marea in centro storico a Venezia
- `Chioggia città - Vigo` (Chioggia), come riferimento per la marea in centro storico a Chioggia
- `Diga Sud Lido e Faro` (San Nicolò), per monitorare la bocca di porto tra Punta Sabbioni e Lido
- `Diga Nord Malamocco` (Malamocco), per monitorare la bocca di porto tra Lido e Pellestrina
- `Diga Sud Chioggia` (Pellestrina), per monitorare la bocca di porto tra Pellestrina e Chioggia

I dati delle stazioni di rilevamento e i relativi grafici per la giornata presa in esame vengono salvati nell'`archivio` nella cartella con la data corrispondente. Sono disponibili alcuni esempi generati con versioni antecedenti del codice. In particolare, la cartella `2019-11-12` è corredata di analisi aggiuntive viste alle maree eccezionali verificatesi quella settimana.

