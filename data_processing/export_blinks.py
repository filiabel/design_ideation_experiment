#%%
import pandas as pd
from glob import glob
import re

#%%
# Read annotations
annots = pd.read_csv('../Processed data/all_annotations.csv')

# Get wordset annotations to map out subsets from data
cols = ['participant_id', 'problem_id','stimuli', 'wordset', 'idea_total','timestamp', 'duration']
subset_annots = annots[annots.label == 'wordset'][cols]

dtypes = {col:'uint8' for col in ['participant_id', 'problem_id','wordset', 'idea_total']}
subset_annots = subset_annots.astype(dtypes)

#%%
# Read and concatinate all blink data files in 001 export folder
files = glob(f'../../Experiment/Data/Pupil data/participant_0*/000/exports/001/blinks.csv')

assert len(files) == 24

# Use only the following columns
usecols = ['id', 'start_timestamp', 'end_timestamp','duration', 'confidence']

dfs = []
for f in files:
    participant_id = int(re.findall('participant_(\d+)', f)[0])
    
    print(f'Reading file for participant {participant_id}')
    df = pd.read_csv(f, usecols=usecols)
    
    # Add column with participant id as unique identifier.
    cols = ['participant_id'] + df.columns.tolist()
    df['participant_id'] = participant_id 
    
    # Convert some column types to save space and then reorder col. order
    dtypes = {'participant_id': 'uint8', 'id':'uint16'}
    df = df.astype(dtypes)[cols]
    
    dfs.append(df)

#%%
df_total = pd.concat(dfs, ignore_index=True)

#%%
# Make annotated subset
subset_mask = [df_total[(df_total.participant_id == t[0]) & (df_total.start_timestamp.between(t[5], sum(t[5:])))] \
                .assign(problem_id=t[1], stimuli=t[2], wordset=t[3], idea_total=t[4]) \
                for t in subset_annots.itertuples(index=False, name=None)]

# Concatenate subset based on mask
data = pd.concat(subset_mask, ignore_index=True)

# Save subset to csv
data.to_csv('../Processed data/annotated_blinks.csv',index=False)


#%%
# Save to csv
df_total.to_csv('../Processed data/all_blinks.csv',index=False)
