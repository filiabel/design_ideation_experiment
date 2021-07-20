# Data processing
This folder contains code used to concatenate raw data exported from Pupil Player into more managable data and code for audio transcription using Google Cloud Speech-to-Text (and Python library SpeechRecognition).

## Export concatenated data
The scripts are written to be run in an interactive Jupyter window, but should run as a normal script as well.

The different scripts creates the following files:
* `export_annotations.py`
  * `all_annotations.csv` - Concatenates all annotation files. This file is used further on for mapping out the different experimental routines.
  * `feedback.csv` - Subset of `all_annotations.csv` containing only the questionnaire feedback for each problem. Also includes a column with the number of ideas generated in during the both wordset routines for the problem.
* `export_[blinks,fixations,gaze,pupillometry].py`
  * `all_*.csv/h5` - Concatenates all files of given type. Using HDF (.h5) for better compression on the larger datasets. Some columns of no significance for further processing were dropped.
  * `annotated_*.csv/h5` - Subset of the `all_*.csv/h5` file containing only the data from the wordset routines, meaning the data during design ideation. Data is annotated with participant/experiment information from `all_annotations.csv`, so that one easily can mask out the wanted data. `idea_total` contains the number of ideas generated in the associated wordset routine.

## Audio transcription
Each wordset routine was recorded to gain insight into what kind of ideas that were generated for each problem, and across the different stimuli. \
In addition to [Google Cloud Speech-to-Text API](https://cloud.google.com/speech-to-text), Python library [SpeechRecognition](https://github.com/Uberi/speech_recognition#readme) was used to obtain an alternative transcription. The library uses a free Google Speech API. 

For the transcription using Google Cloud API, configurations were set such that the words in the current design problem and stimuli words were feeded into the model to potentially improve accuracy. Time offset of each word were also enabled and saved in the JSON response of each API call. Transcriptions were saved in `transcription_dataset.csv` along with experimental info, design problem description and stimuli words.

Automatic transcription is used a preliminary analysis method, as opposed to manually transcribing ~10 hours of audio. As none of the participants were English speakers and many words spoken are technical terms, the speech recognizers does not always return a high confidence transcription. The dataset should therefore be treated as _descriptive_ and not ground truth. 

## XDF to CSV conversion
This is useful for LSL data recorded with LabRecorder, so that it can be parsed to readable CSV files. Other tools for this conversion may also exist, but this a simple code based solutaion. See example code below:
```python
# For pretty printing XDF stream info
import json
import pprint

import pyxdf
import numpy as np
import pandas as pd


# Import XDF file
# This can be done iteratively by looping through files in  folder with e.g. glob
fpath = 'file.xdf'
outpath = 'output.csv'

streams, fileheader = pyxdf.load_xdf(fpath)
print("Found {} streams:".format(len(streams)))

# Set to true to view streams in console
flag_pprint = False

# Extract labels and all channel data for each stream. Assuming each channel has label metadata.
for stream in streams:
    name = stream['info']['name'][0]
    print(f'Stream name: {name}')

    # Pretty print channel info and stream info
    if flag_pprint:
        pprint.pprint(json.loads(json.dumps(stream['info']['desc'][0]['channels'][0]['channel'])))
        pprint.pprint(json.loads(json.dumps(stream['info'])))

    # Extract all labels
    labels = [ch['label'][0] for ch in stream['info']['desc'][0]['channels'][0]['channel']]
    
    # Generate data as dictionary with label as key
    data = {labels[i]: np.asarray(stream['time_series'])[:,i] for i in range(len(labels))}
    data['timestamp'] = stream['time_stamps']

    # Convert to Pandas dataframe
    df = pd.DataFrame(data)

    # Export to csv
    df.to_csv(f"{name}_{outpath}", index=False)



```

