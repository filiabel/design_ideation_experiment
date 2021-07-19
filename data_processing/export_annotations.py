#%%
# Read all annotation file and combine feedback and total ideas per problem for all participants
from glob import glob
import pandas as pd

# Read and concatinate all annotation files in 000 export folder
files = glob(f'../../Experiment/Data/Pupil data/participant_0*/000/exports/000/annotations.csv')
df = pd.concat((pd.read_csv(f, index_col='index') for f in files), ignore_index=True).reset_index(drop=True)
df.to_csv('../Processed data/all_annotations.csv', index=False)

#%%
# Get feedback annotations
feedback_cols = [x for x in df.columns if 'feedback' in x]
df_feedback = df[df['label'] == 'feedback'][['group_id','participant_id', 'problem_id', 'stimuli', *feedback_cols]]

# Sort by participant and problem id
feedback = df_feedback.sort_values(['participant_id', 'problem_id'])

#%%
# Get wordset annotations (containing total ideas per wordset)
df_wordset = df[df['label'] == 'wordset']
ideas_sum = df_wordset.groupby(by=['participant_id', 'problem_id'])['idea_total'].sum().reset_index()

# %%
# Merge on same keys and convert to integers only
result = pd.merge(feedback, ideas_sum, how='inner', on=['participant_id', 'problem_id'])

columns_type = {col:'int32' for col in result.columns if col not in ['stimuli', 'group_id']}
result = result.astype(columns_type)

# %%
# Export as csv
result.to_csv('../Processed data/feedback.csv', index=False)
