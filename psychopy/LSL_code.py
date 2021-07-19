'''
Includes code examples on how to enable LSL functionality in PsychoPy.
More general examples of pylsl can be found here: <https://github.com/chkothe/pylsl/tree/master/examples>
'''
### In a code component 'init' routine or similar.

## Before experiment 
# Import modules from pylsl
from pylsl import StreamInfo, StreamOutlet

## Begin experiment 
# Choose the amounts of channels (columns/data points) you want in your LSL stream from Psychopy. Add as many as you need!
channel_names = ['participant_id','problem_id', 'routine', 'stimuli', 'idea_timestamp'] # ..... etc.

# Creating the LSL stream for PsychoPy
info = StreamInfo(name='psychopy', type='Markers', channel_count=len(channel_names),
                   channel_format='string', source_id='uniqueid12345') 

# Setting channel_format='string' will set all your columns to strings, but at the same time allow for sending all kinds of data.
# Casting to the correct data type can be done when post processing the generated output file in xdf format.

# Add metadata for channels
chns = info.desc().append_child("channels")
for label,ch_type in zip(channel_names, channel_type):
    ch = chns.append_child("channel")
    ch.append_child_value("label", label)

# Initialize the stream so that LabRecorder (or other software) can pick it up.
outlet = StreamOutlet(info)

### Add this in code components whenever you need to send an annotation/marker.

# Make sure the lists passed into outlet.push_sample() has a value for each channel. You can pass empty string values
# Remember that our stream only accepts strings, as this is set as our format. Convert your data: str(4) etc.
# channel_names =  ['participant_id','problem_id', 'routine',        'stimuli', 'idea_timestamp'] # ..... etc.
outlet.push_sample([ participant_id,   str(4),     'idea_generated', '',        ''              ])
