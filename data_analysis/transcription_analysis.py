#%%

# Import libraries
import spacy
import pandas as pd
from collections import Counter

#%%
df = pd.read_csv('Processed data/transcription_dataset.csv').fillna('') # Fill NaN with empty string

# %%
# Group by problem, stimuli and wordset. Concatenate all transcriptions
cols = ['problem_id', 'problem','wordset','stimuli', 'words', 'transcription']
df_grouped = df.groupby(by=cols[:4]).agg({'words':'first', 'transcription':' '.join})

#%%

# Load Spacy. Disable parts of the pipeline
nlp = spacy.load("en_core_web_sm", disable=['parser', 'ner'])

# Add some custom stop words based on preliminary results
custom_stop_words = ['okay','ok', 'like', 'use', 'maybe', 'thing', 'yeah', 'oh']
for stop_word in custom_stop_words:
    nlp.vocab[stop_word].is_stop = True


def get_top_words(doc, n=10):
    # Remove stop words, as well as all token that are punctuation, digits only and whitespace
    words = [token.lemma_.lower() for token in doc \
        if not token.is_stop and not token.is_punct and \
            not token.is_space and not token.is_digit]
    
    # Get n most common words
    word_freq = Counter(words)
    common_words = word_freq.most_common(n)

    # Returns n most popular words as one string   
    return ', '.join([word[0] for word in common_words])

# Add the 10 most frequent words
df_grouped["most_frequent"] = [get_top_words(doc) for doc in nlp.pipe(df_grouped["transcription"].tolist())]
res = df_grouped.reset_index()

# %%

# Look at intersections for each problem/wordset across all stimuli
intersections = []

for problem_id in range(1,13):
    for wordset in [1,2]:
        s = res[(res.problem_id == problem_id) & (res.wordset == wordset)]['most_frequent'].str.split(', ').reset_index(drop=True)
        intersection = ', '.join(set(s[0]) & set(s[1]) & set(s[2]))
        if intersection == '':
            intersection = '-'
        intersections.append(intersection)


df_intersections = df.groupby(by=['problem_id', 'problem','wordset']).first()
df_intersections = pd.DataFrame(index=df_intersections.index)
df_intersections['intersections'] = intersections
df_intersections
# %%
