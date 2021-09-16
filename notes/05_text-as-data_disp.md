# Tekst som data

## Indhold
**Hvorfor tekst?**

**Tekst og machine learning**
- NLP og text mining
    - Mange betegnelser for lignende praksisser: NLP, text mining, computer-assisted text analysis, quantitative text analysis
    - NLP: Få en computer til at forstå det menneskelige sprog (https://play.aidungeon.io/)
    - Text mining: Udlede information om text med computationelle metoder (med brug af NLP)
- Superviseret: Kategoriseringer, sentiment, udlede information
- Usuperviseret: Temaer, grupperinger, ordforbindelser

**Demo: Simpelt eksempel med text mining (netværksvisualisering af klima-tweets)**

**Tekst i Python**
- Hvad er strings?
- Hvordan kan vi arbejde med tekster i Python? (helt simpelt)
- Simple teksthåndteringsmetoder

**ØVELSE 1: Simpel teksthåndtering**

**Pre-processing (med basisfunktioner)**
- Tokenization
- Tegnsætning
- Stopord
- Lowercase
- Ordstammer
- Navneform / infinitv

**Simpel ordtælling**

**ØVELSE 2: Pre-processing og simpel ordtælling**
- Pre-process en enkelt tekst/tekststump
- Optæl ord

**Sprogmodeller (stanza)**
- Hvad er en sprogmodel?
- Brug af stanza
- Indhold i stanza:
    - tokenizer
    - lemmatizer
    - ner
    - sentiment analysis
    - POS-tagging
- Udlede meningsfulde tokens med stanza

**ØVELSE 3: Meningsfulde tokens med stanza**
- Pre-process samme tekst/tekststump med stanza
- Optæl ord

**Tidy text data**
- Hvordan arbejder vi med større tekstsamlinger? (corpora)
- Tidy text data: Token som observation
    - Fordele:
        - Fastholder dokumenttilhør og andre relevante oplysninger
        - Gør det nemt at arbejde med
        - Vi kan bruge metoder, som vi kender fra at arbejde med struktureret data
    - Ulemper: 
        - Data fylder hurtigt meget
        - Kan have effekt på beregningstiden
        - Ofte ikke kompatibelt med andre modeller
        
**Fra text corpora til tidy text**
- Udarbejd tokenizer funktion
- Brug af apply til at tokenize
- Explode til at gøre tidy
- Teknikker til at arbejde med tidy text: `groupby`, `isin`, plots

**ØVELSE 4: Tidy text data (reddit data)**
- Udarbejd tokenizer funktion
- Brug funktion til at tokenize reddit data
- Gør tidy
- Optæl ord via groupby

**Usuperviseret maskinlæring og tekst: topic models**
- Topic models en meget udbredt teknik til at udforske mønstre
- Fordele
    - Overblik, inddeling
- Ulemper
    - Samme som med klynger: ekstern validitet
    - Høj grad af vilkårlighed (hvor mange topics?)
    - Sårbar over for små ændringer i datahåndtering
- Bag-of-words: Ords kontekst ikke inddraget

**Brug af topic models i Python**
- Alternativ vægtning: tf-idf
- Brug af pakken X til topic models
- LDAviz?

**ØVELSE 5: Topic models i Python (reddit data)**
- Forbered data til topic model
- Kør topic model
- Visualiser resultater


## Til FC
- Alternativ vægtning: tf-idf (hurtigt fra tekst til corpus uden brug af sprogmodel til tokenization)
- Subreddit data
- Ord til dummy-variable
- Predict positiv/negativ med random forests