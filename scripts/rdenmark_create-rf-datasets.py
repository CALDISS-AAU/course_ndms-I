import os
import spacy
import pandas as pd
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer

nlp = spacy.load("da_core_news_sm", disable = ['parser', 'ner', 'textcat'])

data_path = os.path.join("D:/", "data", "reddit")
filename = "reddit_rdenmark_q=danmark_01012020-15032021_long.zip"

def tokenizer_spacy(text): # Definerer funktion ud fra koden fra tidligere
    custom_stops = ['gt', 'bare', 'the', 'to', 'når', 'https', 'helt', 'of', 'se', 'in', 'www', 'is', 'you', 'dk', 'får', 'com', 'ret', 'it', 'that', 'år', 'siger',
               'hele', 'går', 'ting', 'ser', 'del', 'vel', 'tage', 'set', 'are', 'be', 'not', 'but', 'amp']
    stop_words = list(nlp.Defaults.stop_words) + custom_stops
    pos_tags = ['PROPN', 'ADJ', 'NOUN']

    doc = nlp(text)

    tokens = []

    for word in doc:
        if (len(word.lemma_) == 1):
            continue
        if (word.pos_ in pos_tags) and (word.lemma_.lower() not in stop_words):
            tokens.append(word.lemma_.lower())
                
    return(tokens)

def return_tokens(tokens):
    return(tokens)

def top50_tfidf(tokens_list, tokenizer = return_tokens):

    vectorizer = TfidfVectorizer(
        tokenizer=return_tokens,
        preprocessor=return_tokens,
        token_pattern=None,
        norm = False)

    transformed_documents = vectorizer.fit_transform(tokens_list)

    transformed_documents_as_array = transformed_documents.toarray()

    df = pd.DataFrame(transformed_documents_as_array, columns = vectorizer.get_feature_names())

    word_tfidfsum = df.sum().sort_values(ascending = False)
    top_words = list(word_tfidfsum.index[0:50])
    
    return(top_words)

def add_token_dummies(df, wordlist):
    
    for word in wordlist:
        colname = "token_{}".format(word)
        df[colname] = df['comment_tokens'].apply(lambda tokens: int(word in tokens))
    
    return(df)


# Load data
reddit_df = pd.read_csv(os.path.join(data_path, filename))


# Data for FC videos
filter_start = int(datetime(2020,1,1,0,0).timestamp())
filter_end = int(datetime(2020,7,1,0,0).timestamp())

reddit_fcv = reddit_df.copy()
reddit_fcv = reddit_fcv.loc[reddit_fcv['post_num_comments'].astype(int) > 5, :]
reddit_fcv = reddit_fcv.loc[(reddit_fcv['post_created_utc'] >= filter_start) & (reddit_fcv['post_created_utc'] < filter_end), :]
reddit_fcv = reddit_fcv.loc[reddit_fcv['comment_body'].str.len() > 30, :]

reddit_fcv['comment_tokens'] = reddit_fcv['comment_body'].apply(tokenizer_spacy)
reddit_fcv = reddit_fcv.loc[reddit_fcv['comment_tokens'].apply(lambda tokens: len(tokens) > 1), :]

reddit_fcv['comment_upvoted'] = reddit_fcv['comment_score'] > 1
reddit_fcv['comment_downvoted'] = reddit_fcv['comment_score'] < 1

fcv_tokens = list(reddit_fcv['comment_tokens'])
fcv_top50 = top50_tfidf(fcv_tokens)

reddit_fcv_dummies = add_token_dummies(reddit_fcv, fcv_top50)

outname = "reddit_rdenmark_q=danmark_01012020-30062020_tokendummies.zip"

reddit_fcv_dummies.to_csv(os.path.join(data_path, outname), index = False, compression = "zip")


# Data for FC exercise
filter_start = int(datetime(2020,7,1,0,0).timestamp())
filter_end = int(datetime(2021,1,1,0,0).timestamp())

reddit_fce = reddit_df.copy()
reddit_fce = reddit_fce.loc[reddit_fce['post_num_comments'].astype(int) > 5, :]
reddit_fce = reddit_fce.loc[(reddit_fce['post_created_utc'] >= filter_start) & (reddit_fce['post_created_utc'] < filter_end), :]
reddit_fce = reddit_fce.loc[reddit_fce['comment_body'].str.len() > 30, :]

reddit_fce['comment_tokens'] = reddit_fce['comment_body'].apply(tokenizer_spacy)
reddit_fce = reddit_fce.loc[reddit_fce['comment_tokens'].apply(lambda tokens: len(tokens) > 1), :]

reddit_fce['comment_upvoted'] = reddit_fce['comment_score'] > 1
reddit_fce['comment_downvoted'] = reddit_fce['comment_score'] < 1

fce_tokens = list(reddit_fce['comment_tokens'])
fce_top50 = top50_tfidf(fce_tokens)

reddit_fce_dummies = add_token_dummies(reddit_fce, fce_top50)

outname = "reddit_rdenmark_q=danmark_01072020-31122020_tokendummies.zip"

reddit_fce_dummies.to_csv(os.path.join(data_path, outname), index = False, compression = "zip")