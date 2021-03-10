import os
import pandas as pd
import stanza
from nltk.corpus import stopwords

data_path = os.path.join("D:/", "data", "poltweets")

stanza.download('da')
nlp = stanza.Pipeline('da', processors = 'tokenize, pos, lemma') 

tweetdata_url = "https://raw.githubusercontent.com/CALDISS-AAU/course_ndms-I/master/datasets/poltweets_sample.csv"
tweets_df = pd.read_csv(tweetdata_url)

def tokenizer_stanza(text):
    custom_stops = ["@"]
    stop_words = list(stopwords.words('danish')) + custom_stops
    pos_tags = ['PROPN', 'ADJ', 'NOUN']

    doc = nlp(text)

    tokens = []

    for sentence in doc.sentences:
        for word in sentence.words:
            if (word.pos in pos_tags) and (word.lemma not in stop_words) and not (word.lemma.startswith("@")):
                tokens.append(word.lemma)
                
    return(tokens)
   
tweets_df['tokens'] = tweets_df['full_text'].apply(tokenizer_stanza)

filename = "poltweets_sample_tokens.csv"
tweets_df.to_csv(os.path.join(data_path, filename), index = False)