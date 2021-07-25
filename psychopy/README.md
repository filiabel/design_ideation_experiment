# Psychopy
Requires installation of [PsychoPy Standalone](https://www.psychopy.org/download.html).

## Running the experiment
By downloading this folder one should be able to run the experiment by opening `design_ideation_final.psyexp` in PsychoPy. But be aware of the following: 
* The experiment was made to run on an 1920x1200 px screen and therefore components are placed accordingly. This can be changed in PsychoPy experiment settings by adding a new monitor calibration for your screen, but does not necessarily result in the same _visual_ result.
* Recording data from Pupil Core eye tracker is a major part of this experiment. If you do not want do this, you will need to remove or comment out a lot of code. This also showcases how PsychoPy communicates with Pupil Capture:
  *  `Begin experiment` tab of `init_code` component in `init` routine establishes connection with Pupil and beginning the recording over the included [Network API](https://docs.pupil-labs.com/developer/core/network-api/). It also defines functionality for sending custom annotations.
  *  `calibration` routine is not necessary unless you need to calibrate mobile eye trackers.
  *  In each routine, there is code component with annotation triggers `Begin routine` and `End routine` for timing functionality.
  *  Annotation triggers with data saving functionality are spread out in these routines: `wordset_*`, `one_back`, `feedback`.
  *  `thanks` routine has code for stopping Pupil recording in the `End routine` tab.
* By default, the experiment records sound on each wordset routine. This can be disabled by setting `mic_on = False` in the `Before experiment` tab of `init_code` component in `init` routine.
  * Audio recording parameters can be set `Begin experiment` of same component as above. Read documentation of [python-sounddevice](https://python-sounddevice.readthedocs.io/en/0.4.2/api/module-defaults.html#sounddevice.default) for additional default parameters.
* `Data` folder is there to preserve the directory structure for saving experimental data, but subfolders defaults as empty. Deleting this can cause unknown errors. 

## LabStreamingLayer (LSL)
> "LSL is an overlay network for real-time exchange of time series between applications, most often used in research environments. LSL has clients for many other languages and platforms that are compatible with each other."

LSL offers great functionality for syncing hardware and software when conducting research experiments. Standalone PsychoPy has the Python interface [pylsl](https://github.com/labstreaminglayer/liblsl-Python) installed by default. LSL was not used in this experiment, as Pupil Network API offered similar functionality for this use case, but will be useful if more hardware is to be included.

LSL interfaces:
* [LabRecorder](https://github.com/labstreaminglayer/App-LabRecorder) - client to choose streams from the network and save to .xdf file.
* [Pupil Capture LSL Relay](https://github.com/labstreaminglayer/App-PupilLabs/blob/master/pupil_capture/README.md) - plugin to send data from Pupil to the LSL stream.
* [Collection of apps and tools for LabStreamingLayer](https://github.com/labstreaminglayer/)

The code below showcases an example on how to implement LSL into PsychoPy for annotations. More general examples of pylsl can be found here [here](https://github.com/chkothe/pylsl/tree/master/examples).


## Code snippets
Useful code snippets that are copied from the experiment code (except LSL annotations)
### Pupil Network API
Used for remote control recording and custom annotations.
```python
'''
Scripts and time synchronization and annotaions - based on: 
 - https://github.com/pupil-labs/pupil-helpers/blob/master/python/pupil_remote_control.py 
 - https://github.com/pupil-labs/pupil-helpers/blob/master/python/remote_annotations.py
'''

# Import libraries for Pupil communication
import zmq
import msgpack as serializer
from time import sleep

# Setup zmq context and remote helper
ctx = zmq.Context()
pupil_remote = zmq.Socket(ctx, zmq.REQ)
pupil_remote.connect("tcp://127.0.0.1:50020")

pupil_remote.send_string("PUB_PORT")
pub_port = pupil_remote.recv_string()
pub_socket = zmq.Socket(ctx, zmq.PUB)
pub_socket.connect("tcp://127.0.0.1:{}".format(pub_port))

# Set time function to Psychopy's globalClock - time since experiment started
time_fn = globalClock.getTime  

# Set Pupil Capture's time base to match Psychopy's experiment clock
pupil_remote.send_string("T {}".format(time_fn()))
print(pupil_remote.recv_string())

sleep(1) '''This was added post-experiment. 
No sleep before record is believed to cause issues with certain plugins in Pupil Player 
due to some data is timestamped with a value much larger than the new zeroed timestamp.
See: https://discord.com/channels/285728493612957698/285728493612957698/857998442999578664
'''
# Function for sending notifications
def notify(notification):
    """Sends ``notification`` to Pupil Remote"""
    topic = "notify." + notification["subject"]
    payload = serializer.dumps(notification, use_bin_type=True)
    pupil_remote.send_string(topic, flags=zmq.SNDMORE)
    pupil_remote.send(payload)
    return pupil_remote.recv_string()

# Packing notification data
def send_trigger(trigger):
    payload = serializer.dumps(trigger, use_bin_type=True)
    pub_socket.send_string(trigger["topic"], flags=zmq.SNDMORE)
    pub_socket.send(payload)

# Start the annotations plugin
notify({"subject": "start_plugin", "name": "Annotation_Capture", "args": {}})

# Start recording - setting filename to participant_id
pupil_remote.send_string(f"R participant_{expInfo['participant']}")
pupil_remote.recv_string()
sleep(0.5)

'''
A lot of the variables used in the triggers are loaded globally from the scope. 
Some are loaded from the xlsx input files and updates on each iteration in the design problem loop. 
E.g. participant_id, word1, wordset, stimuli...
'''

# Minimal trigger - defaults to current time and duration == 0.0
def new_trigger(label, duration=0.0, timestamp=None):
    if timestamp is None:
        timestamp = time_fn()
    return {
        "topic": "annotation",
        "label": label,
        "timestamp": timestamp,
        "duration": duration,
        "participant_id": participant_id,
        "group_id": group_id
    }
    
# Trigger with more info, includes stimuli info. Same default values as above
def new_wordset_trigger(label, duration=0.0, timestamp=None):
    if timestamp is None:
        timestamp = time_fn()
    return {
        "topic": "annotation",
        "label": label,
        "timestamp": timestamp,
        "duration": duration,
        "participant_id": participant_id,
        "group_id": group_id,
        "problem_id": problem_id,
        "stimuli": stimuli,
        "wordset": wordset,
        "word1": word1,
        "word2": word2,
        "word3": word3,
        "word4": word4,
        "word5": word5        
    }
    
# Send annotation with 0.0 duration
annot = new_trigger('initialization')
send_trigger(annot)
sleep(0.1) 

```

### Recording sound
```python
### Setup
import sounddevice as sd    
from scipy.io.wavfile import write as wav_write

# Make and set directory for recordings to be saved
recordingDir = "sound_files/"
os.mkdir(recordingDir)

# Set recording params
fs = 48000
rec_duration = 65 # Record the entire wordet routine + extra in n-back

# Set default parameters
sd.default.samplerate = fs
sd.default.channels = 1 # Mono sound
sd.default.dtype = 'int16' # So that it can be used with speech recognition

### Record - records for set duration
mic_recording = sd.rec(int(rec_duration * fs))

'''
Other stuff happens. Recording is finished..
'''

### Set filename and save file
mic_filename = recordingDir + 'filename.wav'
wav_write(mic_filename, fs, mic_recording)

```

### LSL annotations
```python
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

# Setting channel_format='string' ensures all data must be formatted as strings, but allows for sending all kinds of data.
# Casting back to the correct data type can be done when post processing the generated output file in xdf format.

# Add metadata for channels
chns = info.desc().append_child("channels")
for label in channel_names:
    ch = chns.append_child("channel")
    ch.append_child_value("label", label)

# Initialize the stream so that LabRecorder (or other software) can pick it up.
outlet = StreamOutlet(info)

### Add this in code components whenever you need to send an annotation/marker.

# Make sure the lists passed into outlet.push_sample() has a value for each channel. You can pass empty string values
# Remember that our stream only accepts strings, as this is set as our format. Convert your data: str(4) etc.
# channel_names =  ['participant_id','problem_id', 'routine',        'stimuli', 'idea_timestamp'] # ..... etc.
outlet.push_sample([ participant_id,   str(4),     'idea_generated', '',        ''              ])

```

