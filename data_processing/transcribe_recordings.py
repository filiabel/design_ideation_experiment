"""Transcribe all sound recordings"""
#%%
import json
from pathlib import Path
import re
import pandas as pd

from google.cloud import speech
from google.oauth2 import service_account

import speech_recognition as sr

def transcribe_gcs(gcs_uri, phrases):
    audio = speech.RecognitionAudio(uri=gcs_uri)

    # Add wordset words to recognizer to potentially imporve accuracy
    speech_context = speech.SpeechContext(phrases=phrases)
    
    # Configure with recording parameters and language
    config = speech.RecognitionConfig(
        sample_rate_hertz=48000,
        language_code="en-US",
        enable_word_time_offsets = True,
        speech_contexts = [speech_context]
    )

    # Send request to client
    operation = client.long_running_recognize(config=config, audio=audio)
    response = operation.result(timeout=90)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    output = []
    for result in response.results:
        alternative = result.alternatives[0] 
        output.append(alternative.transcript.strip()) # Remove surplus whitespace
    
    # Join and return subresults into one string
    return ' '.join(output), response


def transcribe_sr(fname):
    audio_file = sr.AudioFile(fname)
    
    with audio_file as source:
      audio_file = recognizer.record(source)
      
    output = recognizer.recognize_google(audio_data=audio_file)

    return output


# Set up of Cloud client
my_credentials = service_account.Credentials.from_service_account_file("../keys.json")
client = speech.SpeechClient(credentials=my_credentials)

# SpeechRecognition client
recognizer = sr.Recognizer()

#%%
# Read in words and problem for excel sheet and perform cleaning
excel = pd.read_excel('../Experiment/master_input.xlsx').iloc[:,:-5]
stims = ['near', 'far', 'cntrl']

design_problems = excel[['problem', 'problem_id']].copy()
for stim in stims:
    design_problems[stim] = excel[[f'{stim}{i+1}' for i in range(5)]].agg(', '.join, axis=1)

design_problems = design_problems.set_index('problem_id')

#%%
# Placeholder for output data
df_data = []

# Define root and path
root = "../Experiment/Data/Sound recordings/"
p = Path(root)

# Iterate through data of each participant
for participant_id in range(1,25):
    print(f'Participant {participant_id}')
    
    # Get all soundfiles for participant
    fnames = list(p.glob(f"participant_{participant_id:03}/*.wav"))

    # Check for all 24 soundfiles
    assert len(fnames) == 24, print('Missing soundfiles?')

    # Transcribe each file
    for fname in fnames:
        # Read info from filename
        problem_id = int(re.findall('problem(\d+)', str(fname))[0])
        wordset = int(re.findall('(\d).wav', str(fname))[0])
        stim = re.findall('_([a-zA-Z]+)_wordset', str(fname))[0]
        
        print(f'\tProblem {problem_id}, wordset {wordset} [{stim}]')

        # Get problem and stimuli words
        problem = design_problems.loc[problem_id]['problem']
        words = design_problems.loc[problem_id][stim.lower()]

        if wordset == 1:
            words = ', '.join(words.split(', ')[:3])

        # Pass all stimuli and problem words to Cloud recognizer to potentially improve accuracy
        # Remove last char == '.' in problem. 
        phrases = problem[:-1].lower().split() + words.split(', ')
        
        gc_fname = 'gs://sound-recordings/Sound recordings/' + fname.relative_to(root).as_posix()
        
        # Transcribe using Google Cloud and SpeechRecognition
        try:
            out_cloud, response = transcribe_gcs(gc_fname, phrases)
        except Exception:
            out_cloud = ''
            print('\t\tError GC')
        
        try:
            out_sr = transcribe_sr(str(fname))
        except Exception:
            out_sr = ''
            print('\t\tError SR') # Could be empty file

        # Save response from API with same name as transcribed file
        with open(f'Processed data/API responses/{fname.stem}.json','w') as f_json:
            response_dict = type(response).to_dict(response)
            json.dump(response_dict, f_json, indent = 4)
        
        # Save transcriptions with experimental info
        df_data.append([participant_id, problem_id, stim, wordset, problem, words, out_cloud, out_sr])

#%%

# Make df
df = pd.DataFrame(df_data, columns=['participant_id', 'problem_id', 'stimuli', 'wordset', \
    'problem', 'words', 'transcription', 'transcription_sr'])

# Sort df
df = df.sort_values(by=['participant_id', 'problem_id', 'wordset'])

# Save df
df.to_csv('Processed data/transcription_dataset.csv', index=False)

# %%
