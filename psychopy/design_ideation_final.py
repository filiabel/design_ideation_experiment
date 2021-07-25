#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on juli 26, 2021, at 01:11
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Set mic related functions on/off
mic_on = True

# Import microphone module for recording
if mic_on:
    import sounddevice as sd    
    from scipy.io.wavfile import write as wav_write

# Import libraries for Pupil communication
import zmq
import msgpack as serializer
from time import sleep


# Import lib for time conversion
import datetime


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'design_ideation'  # from the Builder filename that created this script
expInfo = {'participant': '', 'group': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'Data/Psychopy data/%s_%s' % (expInfo['participant'], expName)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\OneDrive - NTNU\\Design ideation\\Experiment\\design_ideation_final.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1200], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='dellMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "init"
initClock = core.Clock()
# Define constants from exp. input
participant_id = expInfo['participant']
group_id = expInfo['group'].upper()

# Set to debug
# logging.console.setLevel(logging.DEBUG)

if mic_on:
    # Make and set directory for recordings to be saved
    recordingDir = _thisDir + fr"\Data\Sound recordings\participant_{expInfo['participant']}"
    os.mkdir(recordingDir)
    
    # Set recording params
    fs = 48000
    rec_duration = 65 # Record the entire wordet routine + extra in n-back
    
    # Set default parameters
    sd.default.samplerate = fs
    sd.default.channels = 1 # Mono sound
    sd.default.dtype = 'int16' # So that it can be used with speech recognition
    

# Initialize components for Routine "calibration"
calibrationClock = core.Clock()
start_exp = keyboard.Keyboard()
calib_text = visual.TextBox2(
     win, text='Welcome!\nFirst we need to calibrate the eye-tracking device properly. Please follow the instructions given by the researcher.\n\nWhen asked to proceed, please press <SPACE>. ', font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=None, borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='calib_text',
     autoLog=False,
)

# Initialize components for Routine "instr"
instrClock = core.Clock()
instructions = visual.TextBox2(
     win, text='In this experiment you will be asked to come up with concept solutions to open ended design problems.\n\nDuring some problems you may receive a set of words which are intended to serve as inspiration for your concepts. You will see a total of 12 design problems. For each problem you will have 2 minutes to develop as many concepts as you can. \nIn other words, the goal is to generate as many ideas as possible. You do not need to consider realism or whether the concept already exists. You are to think aloud during ideation, that means saying whatever comes into your mind. \n\nEach time you think of a new concept, indicate it by pressing <SPACE>. Please speak English.', font='Open Sans',
     pos=(0,0.12),     letterHeight=0.035,
     size=(1.2,0.5), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='instructions',
     autoLog=True,
)
instr_continue = visual.TextBox2(
     win, text='Press <SPACE> to continue.', font='Open Sans',
     pos=(0.3, -0.40),     letterHeight=0.03,
     size=None, borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=True,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='instr_continue',
     autoLog=True,
)
instr_stop = keyboard.Keyboard()

# Initialize components for Routine "one_back_instr"
one_back_instrClock = core.Clock()
one_back_illustration = visual.ImageStim(
    win=win,
    name='one_back_illustration', 
    image='Media\\\\one_back.png', mask=None,
    ori=0.0, pos=(0.45, 0), size=[0.55],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
one_back_text = visual.TextBox2(
     win, text='Between the design ideation, a simple memory task called "1-back" will be performed. \n\nYour goal is to indicate if a letter is similar to the previous one by pressing <SPACE>. \nIf they are different from each other, no action is required. Each letter will be shown for appx. 2 seconds or until <SPACE> is pressed.\n\nAn example is shown in the illustration to the right.\n\n', font='Open Sans',
     pos=(-0.3, 0),     letterHeight=0.035,
     size=[0.8,0.6], borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='one_back_text',
     autoLog=True,
)
instr_begin = visual.TextBox2(
     win, text='Press <SPACE> to begin the experiment. ', font='Open Sans',
     pos=(0.2, -0.40),     letterHeight=0.03,
     size=None, borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=True,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='instr_begin',
     autoLog=True,
)
one_back_instr_click = keyboard.Keyboard()

# Initialize components for Routine "problem"
problemClock = core.Clock()
design_problem = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=None, borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=True,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='design_problem',
     autoLog=True,
)
title = visual.TextBox2(
     win, text='Consider the following design problem:', font='Open Sans',
     pos=(0, 0.3),     letterHeight=0.05,
     size=None, borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='title',
     autoLog=True,
)

# Initialize components for Routine "crosshair"
crosshairClock = core.Clock()
# Generate 12 random durations for cross between 0.5-4 s
cross_times = list(randint(5,40,12)/10)
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-1.0, interpolate=True)

# Initialize components for Routine "wordset_1"
wordset_1Clock = core.Clock()
problem_1 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(0, 0.3),     letterHeight=0.05,
     size=None, borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='problem_1',
     autoLog=True,
)
skip_1 = keyboard.Keyboard()
press_1 = visual.TextBox2(
     win, text='Press <SPACE> each time you think of a new idea.', font='Open Sans',
     pos=(0.15, -0.4),     letterHeight=0.03,
     size=None, borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=True,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='press_1',
     autoLog=True,
)
border_1 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=(1.3,0.3), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=True,
     lineSpacing=1.0,
     padding=0.1,
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='border_1',
     autoLog=True,
)
word1_1 = visual.TextStim(win=win, name='word1_1',
    text='',
    font='Open Sans',
    pos=(-0.45, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
word2_1 = visual.TextStim(win=win, name='word2_1',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
word3_1 = visual.TextStim(win=win, name='word3_1',
    text='',
    font='Open Sans',
    pos=(0.45, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "one_back_begin"
one_back_beginClock = core.Clock()
one_back_begin_text = visual.TextStim(win=win, name='one_back_begin_text',
    text='1-Back memory task will soon begin.\n\nPress <SPACE> if the letter is similar to the previous one.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
# Init. total number of n-backs and subset of letters
num_one_back = 50
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
one_back_start_letter = visual.TextStim(win=win, name='one_back_start_letter',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "one_back"
one_backClock = core.Clock()
stim_text = visual.TextStim(win=win, name='stim_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "wordset_2"
wordset_2Clock = core.Clock()
problem_2 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(0, 0.3),     letterHeight=0.05,
     size=None, borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='problem_2',
     autoLog=True,
)
skip_2 = keyboard.Keyboard()
press_2 = visual.TextBox2(
     win, text='Press <SPACE> each time you think of a new idea.', font='Open Sans',
     pos=(0.15, -0.4),     letterHeight=0.03,
     size=None, borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=True,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='press_2',
     autoLog=True,
)
border_2 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(0, -0.1),     letterHeight=0.05,
     size=(1.3,0.45), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=True,
     lineSpacing=1.0,
     padding=0.1,
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='border_2',
     autoLog=True,
)
word1_2 = visual.TextStim(win=win, name='word1_2',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
word2_2 = visual.TextStim(win=win, name='word2_2',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
word3_2 = visual.TextStim(win=win, name='word3_2',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
word4_2 = visual.TextStim(win=win, name='word4_2',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
word5_2 = visual.TextStim(win=win, name='word5_2',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
line = visual.TextStim(win=win, name='line',
    text='-  -  -  -  -  -  -',
    font='Open Sans',
    pos=(0, -0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
question_title = visual.TextStim(win=win, name='question_title',
    text='',
    font='Open Sans',
    pos=(0, 0.3), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
min_label = visual.TextStim(win=win, name='min_label',
    text='',
    font='Open Sans',
    pos=(-0.5, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
max_label = visual.TextStim(win=win, name='max_label',
    text='',
    font='Open Sans',
    pos=(0.5, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
one = visual.ImageStim(
    win=win,
    name='one', 
    image='Media\\\\one.png', mask=None,
    ori=0.0, pos=(-0.5, 0), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
two = visual.ImageStim(
    win=win,
    name='two', 
    image='Media\\\\two.png', mask=None,
    ori=0.0, pos=(-0.25, 0), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
three = visual.ImageStim(
    win=win,
    name='three', 
    image='Media\\\\three.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
four = visual.ImageStim(
    win=win,
    name='four', 
    image='Media\\\\four.png', mask=None,
    ori=0.0, pos=(0.25, 0), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
five = visual.ImageStim(
    win=win,
    name='five', 
    image='Media\\\\five.png', mask=None,
    ori=0.0, pos=(0.5, 0), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
instr_feedback = visual.TextBox2(
     win, text='Use the mouse and left-click your rating of choice.', font='Open Sans',
     pos=(0.15, -0.4),     letterHeight=0.03,
     size=None, borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=True,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='instr_feedback',
     autoLog=True,
)
feedback_click = event.Mouse(win=win)
x, y = [None, None]
feedback_click.mouseClock = core.Clock()
# Define mapping from string to int
word2int = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

# Initialize components for Routine "one_back_begin"
one_back_beginClock = core.Clock()
one_back_begin_text = visual.TextStim(win=win, name='one_back_begin_text',
    text='1-Back memory task will soon begin.\n\nPress <SPACE> if the letter is similar to the previous one.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
# Init. total number of n-backs and subset of letters
num_one_back = 50
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
one_back_start_letter = visual.TextStim(win=win, name='one_back_start_letter',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "one_back"
one_backClock = core.Clock()
stim_text = visual.TextStim(win=win, name='stim_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "save_rec"
save_recClock = core.Clock()

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thanks_text = visual.TextStim(win=win, name='thanks_text',
    text='',
    font='Open Sans',
    pos=(0, 0.1), height=0.08, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
time_text = visual.TextStim(win=win, name='time_text',
    text='',
    font='Open Sans',
    pos=(0, -0.1), height=0.08, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "init"-------
continueRoutine = True
# update component parameters for each repeat
print('Init')

'''
Scripts and time synchronization and annotaions - based on: 
 - https://github.com/pupil-labs/pupil-helpers/blob/master/python/pupil_remote_control.py 
 - https://github.com/pupil-labs/pupil-helpers/blob/master/python/remote_annotations.py
'''

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

sleep(1) 
'''This was added post-experiment. 
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

# Send annotation
annot = new_trigger('initialization')
send_trigger(annot)
sleep(0.1) 
# keep track of which components have finished
initComponents = []
for thisComponent in initComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
initClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "init"-------
while continueRoutine:
    # get current time
    t = initClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=initClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in initComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "init"-------
for thisComponent in initComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "init" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "calibration"-------
continueRoutine = True
# update component parameters for each repeat
# Start time
annot_start = time_fn()

print('Calibration')
start_exp.keys = []
start_exp.rt = []
_start_exp_allKeys = []
# keep track of which components have finished
calibrationComponents = [start_exp, calib_text]
for thisComponent in calibrationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
calibrationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "calibration"-------
while continueRoutine:
    # get current time
    t = calibrationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=calibrationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_exp* updates
    waitOnFlip = False
    if start_exp.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        start_exp.frameNStart = frameN  # exact frame index
        start_exp.tStart = t  # local t and not account for scr refresh
        start_exp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_exp, 'tStartRefresh')  # time at next scr refresh
        start_exp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start_exp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start_exp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_exp.status == STARTED and not waitOnFlip:
        theseKeys = start_exp.getKeys(keyList=['space'], waitRelease=False)
        _start_exp_allKeys.extend(theseKeys)
        if len(_start_exp_allKeys):
            start_exp.keys = _start_exp_allKeys[-1].name  # just the last key pressed
            start_exp.rt = _start_exp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *calib_text* updates
    if calib_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        calib_text.frameNStart = frameN  # exact frame index
        calib_text.tStart = t  # local t and not account for scr refresh
        calib_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(calib_text, 'tStartRefresh')  # time at next scr refresh
        calib_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in calibrationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "calibration"-------
for thisComponent in calibrationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Stop time and send routine annotation
annot_stop = time_fn()
duration = annot_stop - annot_start

annot = new_trigger('calibration', duration, annot_start)
send_trigger(annot)
sleep(0.1) 


# the Routine "calibration" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr"-------
continueRoutine = True
# update component parameters for each repeat
instr_stop.keys = []
instr_stop.rt = []
_instr_stop_allKeys = []
# Start time
annot_start = time_fn()

print('Instructions')

# keep track of which components have finished
instrComponents = [instructions, instr_continue, instr_stop]
for thisComponent in instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr"-------
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions* updates
    if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions.frameNStart = frameN  # exact frame index
        instructions.tStart = t  # local t and not account for scr refresh
        instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
        instructions.setAutoDraw(True)
    
    # *instr_continue* updates
    if instr_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_continue.frameNStart = frameN  # exact frame index
        instr_continue.tStart = t  # local t and not account for scr refresh
        instr_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_continue, 'tStartRefresh')  # time at next scr refresh
        instr_continue.setAutoDraw(True)
    
    # *instr_stop* updates
    if instr_stop.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_stop.frameNStart = frameN  # exact frame index
        instr_stop.tStart = t  # local t and not account for scr refresh
        instr_stop.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_stop, 'tStartRefresh')  # time at next scr refresh
        instr_stop.status = STARTED
        # keyboard checking is just starting
        instr_stop.clock.reset()  # now t=0
        instr_stop.clearEvents(eventType='keyboard')
    if instr_stop.status == STARTED:
        theseKeys = instr_stop.getKeys(keyList=['space'], waitRelease=False)
        _instr_stop_allKeys.extend(theseKeys)
        if len(_instr_stop_allKeys):
            instr_stop.keys = _instr_stop_allKeys[-1].name  # just the last key pressed
            instr_stop.rt = _instr_stop_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Stop time and send routine annotation
annot_stop = time_fn()
duration = annot_stop - annot_start

annot = new_trigger('instructions', duration, annot_start)
send_trigger(annot)
sleep(0.1) 

# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "one_back_instr"-------
continueRoutine = True
# update component parameters for each repeat
one_back_instr_click.keys = []
one_back_instr_click.rt = []
_one_back_instr_click_allKeys = []
# Start time
annot_start = time_fn()

print('1-back instructions')
# keep track of which components have finished
one_back_instrComponents = [one_back_illustration, one_back_text, instr_begin, one_back_instr_click]
for thisComponent in one_back_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
one_back_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "one_back_instr"-------
while continueRoutine:
    # get current time
    t = one_back_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=one_back_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *one_back_illustration* updates
    if one_back_illustration.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        one_back_illustration.frameNStart = frameN  # exact frame index
        one_back_illustration.tStart = t  # local t and not account for scr refresh
        one_back_illustration.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(one_back_illustration, 'tStartRefresh')  # time at next scr refresh
        one_back_illustration.setAutoDraw(True)
    
    # *one_back_text* updates
    if one_back_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        one_back_text.frameNStart = frameN  # exact frame index
        one_back_text.tStart = t  # local t and not account for scr refresh
        one_back_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(one_back_text, 'tStartRefresh')  # time at next scr refresh
        one_back_text.setAutoDraw(True)
    
    # *instr_begin* updates
    if instr_begin.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_begin.frameNStart = frameN  # exact frame index
        instr_begin.tStart = t  # local t and not account for scr refresh
        instr_begin.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_begin, 'tStartRefresh')  # time at next scr refresh
        instr_begin.setAutoDraw(True)
    
    # *one_back_instr_click* updates
    waitOnFlip = False
    if one_back_instr_click.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        one_back_instr_click.frameNStart = frameN  # exact frame index
        one_back_instr_click.tStart = t  # local t and not account for scr refresh
        one_back_instr_click.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(one_back_instr_click, 'tStartRefresh')  # time at next scr refresh
        one_back_instr_click.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(one_back_instr_click.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(one_back_instr_click.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if one_back_instr_click.status == STARTED and not waitOnFlip:
        theseKeys = one_back_instr_click.getKeys(keyList=['space'], waitRelease=False)
        _one_back_instr_click_allKeys.extend(theseKeys)
        if len(_one_back_instr_click_allKeys):
            one_back_instr_click.keys = _one_back_instr_click_allKeys[-1].name  # just the last key pressed
            one_back_instr_click.rt = _one_back_instr_click_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in one_back_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "one_back_instr"-------
for thisComponent in one_back_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Stop time and send routine annotation
annot_stop = time_fn()
duration = annot_stop - annot_start

annot = new_trigger('oneback-instructions', duration, annot_start)
send_trigger(annot)
sleep(0.1) 


# the Routine "one_back_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
design_problems = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(f"input_{expInfo['group']}.xlsx"),
    seed=None, name='design_problems')
thisExp.addLoop(design_problems)  # add the loop to the experiment
thisDesign_problem = design_problems.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDesign_problem.rgb)
if thisDesign_problem != None:
    for paramName in thisDesign_problem:
        exec('{} = thisDesign_problem[paramName]'.format(paramName))

for thisDesign_problem in design_problems:
    currentLoop = design_problems
    # abbreviate parameter names if possible (e.g. rgb = thisDesign_problem.rgb)
    if thisDesign_problem != None:
        for paramName in thisDesign_problem:
            exec('{} = thisDesign_problem[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "problem"-------
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    design_problem.setText(problem)
    # Start time
    annot_start = time_fn()
    
    print(f'Problem {design_problems.thisN+1}')
    
    # keep track of which components have finished
    problemComponents = [design_problem, title]
    for thisComponent in problemComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    problemClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "problem"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = problemClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=problemClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *design_problem* updates
        if design_problem.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            design_problem.frameNStart = frameN  # exact frame index
            design_problem.tStart = t  # local t and not account for scr refresh
            design_problem.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(design_problem, 'tStartRefresh')  # time at next scr refresh
            design_problem.setAutoDraw(True)
        if design_problem.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > design_problem.tStartRefresh + 7.0-frameTolerance:
                # keep track of stop time/frame for later
                design_problem.tStop = t  # not accounting for scr refresh
                design_problem.frameNStop = frameN  # exact frame index
                win.timeOnFlip(design_problem, 'tStopRefresh')  # time at next scr refresh
                design_problem.setAutoDraw(False)
        
        # *title* updates
        if title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            title.frameNStart = frameN  # exact frame index
            title.tStart = t  # local t and not account for scr refresh
            title.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(title, 'tStartRefresh')  # time at next scr refresh
            title.setAutoDraw(True)
        if title.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > title.tStartRefresh + 7.0-frameTolerance:
                # keep track of stop time/frame for later
                title.tStop = t  # not accounting for scr refresh
                title.frameNStop = frameN  # exact frame index
                win.timeOnFlip(title, 'tStopRefresh')  # time at next scr refresh
                title.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in problemComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "problem"-------
    for thisComponent in problemComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Stop time and send routine annotation
    annot_stop = time_fn()
    duration = annot_stop - annot_start
    
    annot = new_trigger(f'problem statement', duration, annot_start)
    annot['problem_id'] = problem_id
    send_trigger(annot)
    sleep(0.1) 
    
    
    # ------Prepare to start Routine "crosshair"-------
    continueRoutine = True
    # update component parameters for each repeat
    # Popping random time from randomized duration list
    cross_duration = cross_times.pop()
    
    # Send routine annotation
    annot = new_trigger('crosshair', cross_duration)
    send_trigger(annot)
    sleep(0.1) 
    
    # keep track of which components have finished
    crosshairComponents = [cross]
    for thisComponent in crosshairComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    crosshairClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "crosshair"-------
    while continueRoutine:
        # get current time
        t = crosshairClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=crosshairClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross* updates
        if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross.frameNStart = frameN  # exact frame index
            cross.tStart = t  # local t and not account for scr refresh
            cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
            cross.setAutoDraw(True)
        if cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross.tStartRefresh + cross_duration-frameTolerance:
                # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cross, 'tStopRefresh')  # time at next scr refresh
                cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in crosshairComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "crosshair"-------
    for thisComponent in crosshairComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "crosshair" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "wordset_1"-------
    continueRoutine = True
    routineTimer.add(60.000000)
    # update component parameters for each repeat
    problem_1.setText(problem)
    skip_1.keys = []
    skip_1.rt = []
    _skip_1_allKeys = []
    # Init. counters and constants
    num_ideas = 0
    wordset = 1
    
    # Start time
    annot_start = time_fn()
    
    print('Wordset 1')
    
    if mic_on:
        # Start sound recording
        mic_recording_1 = sd.rec(int(rec_duration * fs))
    word1_1.setText(word1)
    word2_1.setText(word2)
    word3_1.setText(word3)
    # keep track of which components have finished
    wordset_1Components = [problem_1, skip_1, press_1, border_1, word1_1, word2_1, word3_1]
    for thisComponent in wordset_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    wordset_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "wordset_1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = wordset_1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=wordset_1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *problem_1* updates
        if problem_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            problem_1.frameNStart = frameN  # exact frame index
            problem_1.tStart = t  # local t and not account for scr refresh
            problem_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(problem_1, 'tStartRefresh')  # time at next scr refresh
            problem_1.setAutoDraw(True)
        if problem_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > problem_1.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                problem_1.tStop = t  # not accounting for scr refresh
                problem_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(problem_1, 'tStopRefresh')  # time at next scr refresh
                problem_1.setAutoDraw(False)
        
        # *skip_1* updates
        waitOnFlip = False
        if skip_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            skip_1.frameNStart = frameN  # exact frame index
            skip_1.tStart = t  # local t and not account for scr refresh
            skip_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(skip_1, 'tStartRefresh')  # time at next scr refresh
            skip_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(skip_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(skip_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if skip_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > skip_1.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                skip_1.tStop = t  # not accounting for scr refresh
                skip_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(skip_1, 'tStopRefresh')  # time at next scr refresh
                skip_1.status = FINISHED
        if skip_1.status == STARTED and not waitOnFlip:
            theseKeys = skip_1.getKeys(keyList=['right'], waitRelease=False)
            _skip_1_allKeys.extend(theseKeys)
            if len(_skip_1_allKeys):
                skip_1.keys = _skip_1_allKeys[-1].name  # just the last key pressed
                skip_1.rt = _skip_1_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # Check for idea generations and send annotations
        if 'space' in defaultKeyboard.getKeys(['space']):
            time = wordset_1Clock.getTime()
            
            if time > 0.1: # Not record presses from early on
                annot = new_wordset_trigger('idea')
                annot['idea_timestamp'] = time
                
                send_trigger(annot)
                sleep(0.1) 
                
                num_ideas += 1
                
            
        
        # *press_1* updates
        if press_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            press_1.frameNStart = frameN  # exact frame index
            press_1.tStart = t  # local t and not account for scr refresh
            press_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(press_1, 'tStartRefresh')  # time at next scr refresh
            press_1.setAutoDraw(True)
        if press_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > press_1.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                press_1.tStop = t  # not accounting for scr refresh
                press_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(press_1, 'tStopRefresh')  # time at next scr refresh
                press_1.setAutoDraw(False)
        
        # *border_1* updates
        if border_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            border_1.frameNStart = frameN  # exact frame index
            border_1.tStart = t  # local t and not account for scr refresh
            border_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(border_1, 'tStartRefresh')  # time at next scr refresh
            border_1.setAutoDraw(True)
        if border_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > border_1.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                border_1.tStop = t  # not accounting for scr refresh
                border_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(border_1, 'tStopRefresh')  # time at next scr refresh
                border_1.setAutoDraw(False)
        
        # *word1_1* updates
        if word1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            word1_1.frameNStart = frameN  # exact frame index
            word1_1.tStart = t  # local t and not account for scr refresh
            word1_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(word1_1, 'tStartRefresh')  # time at next scr refresh
            word1_1.setAutoDraw(True)
        if word1_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > word1_1.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                word1_1.tStop = t  # not accounting for scr refresh
                word1_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(word1_1, 'tStopRefresh')  # time at next scr refresh
                word1_1.setAutoDraw(False)
        
        # *word2_1* updates
        if word2_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            word2_1.frameNStart = frameN  # exact frame index
            word2_1.tStart = t  # local t and not account for scr refresh
            word2_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(word2_1, 'tStartRefresh')  # time at next scr refresh
            word2_1.setAutoDraw(True)
        if word2_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > word2_1.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                word2_1.tStop = t  # not accounting for scr refresh
                word2_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(word2_1, 'tStopRefresh')  # time at next scr refresh
                word2_1.setAutoDraw(False)
        
        # *word3_1* updates
        if word3_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            word3_1.frameNStart = frameN  # exact frame index
            word3_1.tStart = t  # local t and not account for scr refresh
            word3_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(word3_1, 'tStartRefresh')  # time at next scr refresh
            word3_1.setAutoDraw(True)
        if word3_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > word3_1.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                word3_1.tStop = t  # not accounting for scr refresh
                word3_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(word3_1, 'tStopRefresh')  # time at next scr refresh
                word3_1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wordset_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "wordset_1"-------
    for thisComponent in wordset_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Stop time
    annot_stop = time_fn()
    duration = annot_stop - annot_start
    
    # Send annotations
    annot = new_wordset_trigger('wordset', duration, annot_start)
    annot['idea_total'] = num_ideas
    
    send_trigger(annot)
    sleep(0.1) 
    
    
    
    # ------Prepare to start Routine "one_back_begin"-------
    continueRoutine = True
    routineTimer.add(7.750000)
    # update component parameters for each repeat
    print('1-back setup')
    
    # Init. counters to zero
    correct = 0
    total = 0
    
    # Init. letters for oneback
    p = 0.4 # Prob. of "true" stim
    bool_mask = randchoice([True, False], size=(num_one_back),p=[p,1-p])
    
    first_letter = randchoice(letters)
    one_back_stim = []
    
    # Generate letters for oneback
    for i in range(num_one_back): 
        prev_stim = first_letter if i == 0 else one_back_stim[i-1]
        
        if bool_mask[i]:    
            one_back_stim.append(prev_stim)
        else:
            new_stim = randchoice([x for x in letters if x!= prev_stim])
            one_back_stim.append(new_stim)
    one_back_start_letter.setText(first_letter)
    # keep track of which components have finished
    one_back_beginComponents = [one_back_begin_text, one_back_start_letter]
    for thisComponent in one_back_beginComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    one_back_beginClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "one_back_begin"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = one_back_beginClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=one_back_beginClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *one_back_begin_text* updates
        if one_back_begin_text.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            one_back_begin_text.frameNStart = frameN  # exact frame index
            one_back_begin_text.tStart = t  # local t and not account for scr refresh
            one_back_begin_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(one_back_begin_text, 'tStartRefresh')  # time at next scr refresh
            one_back_begin_text.setAutoDraw(True)
        if one_back_begin_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > one_back_begin_text.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                one_back_begin_text.tStop = t  # not accounting for scr refresh
                one_back_begin_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(one_back_begin_text, 'tStopRefresh')  # time at next scr refresh
                one_back_begin_text.setAutoDraw(False)
        
        # *one_back_start_letter* updates
        if one_back_start_letter.status == NOT_STARTED and tThisFlip >= 5.75-frameTolerance:
            # keep track of start time/frame for later
            one_back_start_letter.frameNStart = frameN  # exact frame index
            one_back_start_letter.tStart = t  # local t and not account for scr refresh
            one_back_start_letter.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(one_back_start_letter, 'tStartRefresh')  # time at next scr refresh
            one_back_start_letter.setAutoDraw(True)
        if one_back_start_letter.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > one_back_start_letter.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                one_back_start_letter.tStop = t  # not accounting for scr refresh
                one_back_start_letter.frameNStop = frameN  # exact frame index
                win.timeOnFlip(one_back_start_letter, 'tStopRefresh')  # time at next scr refresh
                one_back_start_letter.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in one_back_beginComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "one_back_begin"-------
    for thisComponent in one_back_beginComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Begin timer after first_letter
    one_back_timer = core.CountdownTimer(22)
    
    annot_start = time_fn()
    
    # set up handler to look after randomisation of conditions etc
    one_back_loop_one = data.TrialHandler(nReps=num_one_back, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='one_back_loop_one')
    thisExp.addLoop(one_back_loop_one)  # add the loop to the experiment
    thisOne_back_loop_one = one_back_loop_one.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisOne_back_loop_one.rgb)
    if thisOne_back_loop_one != None:
        for paramName in thisOne_back_loop_one:
            exec('{} = thisOne_back_loop_one[paramName]'.format(paramName))
    
    for thisOne_back_loop_one in one_back_loop_one:
        currentLoop = one_back_loop_one
        # abbreviate parameter names if possible (e.g. rgb = thisOne_back_loop_one.rgb)
        if thisOne_back_loop_one != None:
            for paramName in thisOne_back_loop_one:
                exec('{} = thisOne_back_loop_one[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "one_back"-------
        continueRoutine = True
        # update component parameters for each repeat
        # Set n to current iter in one-back loop
        n = currentLoop.thisN
        
        # Init stims.
        curr_stim = one_back_stim[n]
        prev_stim = first_letter if n == 0 else one_back_stim[n-1]
        
        
        
        stim_text.setText(curr_stim)
        # keep track of which components have finished
        one_backComponents = [stim_text]
        for thisComponent in one_backComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        one_backClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "one_back"-------
        while continueRoutine:
            # get current time
            t = one_backClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=one_backClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Stop when one-back task timer is up
            if one_back_timer.getTime() < 0: 
                # Send one-back routine annotations
                annot_stop = time_fn()
                duration = annot_stop - annot_start
                
                annot = new_trigger('oneback', duration, annot_start)
                annot['problem_id'] = problem_id
                annot['oneback_correct'] = correct
                annot['oneback_total'] = total
                annot['oneback_score'] = correct/total
                send_trigger(annot)
                sleep(0.1) 
               
                continueRoutine = False
                currentLoop.finished = True
                    
            # Max 2 seconds per letter
            if one_backClock.getTime() >= 2.0:
                if not bool_mask[n]: #curr_stim != prev_stim:
                    correct += 1
                    total += 1 
                else:
                    total += 1
                
                continueRoutine = False
            
            # Check for space key press (and right for skip)
            press_time = one_backClock.getTime()
            pressed_keys = defaultKeyboard.getKeys(['space', 'right'])
            
            if 'space' in pressed_keys and press_time >= 0.25:
                if bool_mask[n]: #curr_stim == prev_stim:
                    # Add only reaction time for correct "pushes"
                    reaction_time = press_time - 0.25 #due to 0.25 delay
                   
                    # Send annotation with reaction time
                    annot = new_trigger('oneback_reaction')
                    annot['problem_id'] = problem_id
                    annot['oneback_reactiontime'] = reaction_time
                    send_trigger(annot)
                    sleep(0.05) 
            
                    correct += 1
                    total += 1 
                else: 
                    total += 1
                    
                continueRoutine = False
             
            # For skipping
            if 'right' in pressed_keys:
                continueRoutine = False
                currentLoop.finished = True
            
            # *stim_text* updates
            if stim_text.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
                # keep track of start time/frame for later
                stim_text.frameNStart = frameN  # exact frame index
                stim_text.tStart = t  # local t and not account for scr refresh
                stim_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_text, 'tStartRefresh')  # time at next scr refresh
                stim_text.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in one_backComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "one_back"-------
        for thisComponent in one_backComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "one_back" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed num_one_back repeats of 'one_back_loop_one'
    
    
    # ------Prepare to start Routine "wordset_2"-------
    continueRoutine = True
    routineTimer.add(60.000000)
    # update component parameters for each repeat
    problem_2.setText(problem)
    skip_2.keys = []
    skip_2.rt = []
    _skip_2_allKeys = []
    # Init. counters and constants
    num_ideas = 0
    wordset = 2
    
    # Screen coordinates for words
    firstRow_y = 0.03
    secondRow_y = -0.22
    
    # Set start time
    annot_start = time_fn()
    
    print('Wordset 2')
    
    if mic_on:
        # Start sound recording
        mic_recording_2 = sd.rec(int(rec_duration * fs))
    word1_2.setPos((-0.45, firstRow_y))
    word1_2.setText(word1)
    word2_2.setPos((0, firstRow_y))
    word2_2.setText(word2)
    word3_2.setPos((0.45, firstRow_y))
    word3_2.setText(word3)
    word4_2.setPos((-0.25, secondRow_y))
    word4_2.setText(word4)
    word5_2.setPos((0.25, secondRow_y))
    word5_2.setText(word5)
    # keep track of which components have finished
    wordset_2Components = [problem_2, skip_2, press_2, border_2, word1_2, word2_2, word3_2, word4_2, word5_2, line]
    for thisComponent in wordset_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    wordset_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "wordset_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = wordset_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=wordset_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *problem_2* updates
        if problem_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            problem_2.frameNStart = frameN  # exact frame index
            problem_2.tStart = t  # local t and not account for scr refresh
            problem_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(problem_2, 'tStartRefresh')  # time at next scr refresh
            problem_2.setAutoDraw(True)
        if problem_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > problem_2.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                problem_2.tStop = t  # not accounting for scr refresh
                problem_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(problem_2, 'tStopRefresh')  # time at next scr refresh
                problem_2.setAutoDraw(False)
        
        # *skip_2* updates
        waitOnFlip = False
        if skip_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            skip_2.frameNStart = frameN  # exact frame index
            skip_2.tStart = t  # local t and not account for scr refresh
            skip_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(skip_2, 'tStartRefresh')  # time at next scr refresh
            skip_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(skip_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(skip_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if skip_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > skip_2.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                skip_2.tStop = t  # not accounting for scr refresh
                skip_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(skip_2, 'tStopRefresh')  # time at next scr refresh
                skip_2.status = FINISHED
        if skip_2.status == STARTED and not waitOnFlip:
            theseKeys = skip_2.getKeys(keyList=['right'], waitRelease=False)
            _skip_2_allKeys.extend(theseKeys)
            if len(_skip_2_allKeys):
                skip_2.keys = _skip_2_allKeys[-1].name  # just the last key pressed
                skip_2.rt = _skip_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # Check for ideas generated and send annotations
        if 'space' in defaultKeyboard.getKeys(['space']):
            time = wordset_2Clock.getTime()
            
            if time > 0.5: # Not record presses from early on (as one-back)
                annot_time = time_fn()
                annot = new_wordset_trigger('idea', timestamp=annot_time)
                annot['idea_timestamp'] = time
                
                send_trigger(annot)
                sleep(0.1) 
                
                num_ideas += 1
            
        
        # *press_2* updates
        if press_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            press_2.frameNStart = frameN  # exact frame index
            press_2.tStart = t  # local t and not account for scr refresh
            press_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(press_2, 'tStartRefresh')  # time at next scr refresh
            press_2.setAutoDraw(True)
        if press_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > press_2.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                press_2.tStop = t  # not accounting for scr refresh
                press_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(press_2, 'tStopRefresh')  # time at next scr refresh
                press_2.setAutoDraw(False)
        
        # *border_2* updates
        if border_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            border_2.frameNStart = frameN  # exact frame index
            border_2.tStart = t  # local t and not account for scr refresh
            border_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(border_2, 'tStartRefresh')  # time at next scr refresh
            border_2.setAutoDraw(True)
        if border_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > border_2.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                border_2.tStop = t  # not accounting for scr refresh
                border_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(border_2, 'tStopRefresh')  # time at next scr refresh
                border_2.setAutoDraw(False)
        
        # *word1_2* updates
        if word1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            word1_2.frameNStart = frameN  # exact frame index
            word1_2.tStart = t  # local t and not account for scr refresh
            word1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(word1_2, 'tStartRefresh')  # time at next scr refresh
            word1_2.setAutoDraw(True)
        if word1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > word1_2.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                word1_2.tStop = t  # not accounting for scr refresh
                word1_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(word1_2, 'tStopRefresh')  # time at next scr refresh
                word1_2.setAutoDraw(False)
        
        # *word2_2* updates
        if word2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            word2_2.frameNStart = frameN  # exact frame index
            word2_2.tStart = t  # local t and not account for scr refresh
            word2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(word2_2, 'tStartRefresh')  # time at next scr refresh
            word2_2.setAutoDraw(True)
        if word2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > word2_2.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                word2_2.tStop = t  # not accounting for scr refresh
                word2_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(word2_2, 'tStopRefresh')  # time at next scr refresh
                word2_2.setAutoDraw(False)
        
        # *word3_2* updates
        if word3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            word3_2.frameNStart = frameN  # exact frame index
            word3_2.tStart = t  # local t and not account for scr refresh
            word3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(word3_2, 'tStartRefresh')  # time at next scr refresh
            word3_2.setAutoDraw(True)
        if word3_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > word3_2.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                word3_2.tStop = t  # not accounting for scr refresh
                word3_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(word3_2, 'tStopRefresh')  # time at next scr refresh
                word3_2.setAutoDraw(False)
        
        # *word4_2* updates
        if word4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            word4_2.frameNStart = frameN  # exact frame index
            word4_2.tStart = t  # local t and not account for scr refresh
            word4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(word4_2, 'tStartRefresh')  # time at next scr refresh
            word4_2.setAutoDraw(True)
        if word4_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > word4_2.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                word4_2.tStop = t  # not accounting for scr refresh
                word4_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(word4_2, 'tStopRefresh')  # time at next scr refresh
                word4_2.setAutoDraw(False)
        
        # *word5_2* updates
        if word5_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            word5_2.frameNStart = frameN  # exact frame index
            word5_2.tStart = t  # local t and not account for scr refresh
            word5_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(word5_2, 'tStartRefresh')  # time at next scr refresh
            word5_2.setAutoDraw(True)
        if word5_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > word5_2.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                word5_2.tStop = t  # not accounting for scr refresh
                word5_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(word5_2, 'tStopRefresh')  # time at next scr refresh
                word5_2.setAutoDraw(False)
        
        # *line* updates
        if line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            line.frameNStart = frameN  # exact frame index
            line.tStart = t  # local t and not account for scr refresh
            line.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(line, 'tStartRefresh')  # time at next scr refresh
            line.setAutoDraw(True)
        if line.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > line.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                line.tStop = t  # not accounting for scr refresh
                line.frameNStop = frameN  # exact frame index
                win.timeOnFlip(line, 'tStopRefresh')  # time at next scr refresh
                line.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wordset_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "wordset_2"-------
    for thisComponent in wordset_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Stop time
    annot_stop = time_fn()
    duration = annot_stop - annot_start
    
    #  Send annotation
    annot = new_wordset_trigger('wordset', duration, annot_start)
    annot['idea_total'] = num_ideas
    
    send_trigger(annot)
    sleep(0.1) 
    
    
    
    # set up handler to look after randomisation of conditions etc
    feedback_questions = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('questions.xlsx'),
        seed=None, name='feedback_questions')
    thisExp.addLoop(feedback_questions)  # add the loop to the experiment
    thisFeedback_question = feedback_questions.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFeedback_question.rgb)
    if thisFeedback_question != None:
        for paramName in thisFeedback_question:
            exec('{} = thisFeedback_question[paramName]'.format(paramName))
    
    for thisFeedback_question in feedback_questions:
        currentLoop = feedback_questions
        # abbreviate parameter names if possible (e.g. rgb = thisFeedback_question.rgb)
        if thisFeedback_question != None:
            for paramName in thisFeedback_question:
                exec('{} = thisFeedback_question[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "feedback"-------
        continueRoutine = True
        # update component parameters for each repeat
        question_title.setText(question)
        min_label.setText(label_min.split(' ')[0] + '\n' + label_min.split(' ')[1])
        max_label.setText(label_max.split(' ')[0] + '\n' + label_min.split(' ')[1])
        # setup some python lists for storing info about the feedback_click
        feedback_click.clicked_name = []
        gotValidClick = False  # until a click is received
        # Set start time only on first question
        if feedback_questions.thisN == 0:
            print('Feedback')
            annot_start = time_fn()
            answers = []
        # keep track of which components have finished
        feedbackComponents = [question_title, min_label, max_label, one, two, three, four, five, instr_feedback, feedback_click]
        for thisComponent in feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "feedback"-------
        while continueRoutine:
            # get current time
            t = feedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *question_title* updates
            if question_title.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                question_title.frameNStart = frameN  # exact frame index
                question_title.tStart = t  # local t and not account for scr refresh
                question_title.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question_title, 'tStartRefresh')  # time at next scr refresh
                question_title.setAutoDraw(True)
            
            # *min_label* updates
            if min_label.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                min_label.frameNStart = frameN  # exact frame index
                min_label.tStart = t  # local t and not account for scr refresh
                min_label.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(min_label, 'tStartRefresh')  # time at next scr refresh
                min_label.setAutoDraw(True)
            
            # *max_label* updates
            if max_label.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                max_label.frameNStart = frameN  # exact frame index
                max_label.tStart = t  # local t and not account for scr refresh
                max_label.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(max_label, 'tStartRefresh')  # time at next scr refresh
                max_label.setAutoDraw(True)
            
            # *one* updates
            if one.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                one.frameNStart = frameN  # exact frame index
                one.tStart = t  # local t and not account for scr refresh
                one.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(one, 'tStartRefresh')  # time at next scr refresh
                one.setAutoDraw(True)
            
            # *two* updates
            if two.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                two.frameNStart = frameN  # exact frame index
                two.tStart = t  # local t and not account for scr refresh
                two.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(two, 'tStartRefresh')  # time at next scr refresh
                two.setAutoDraw(True)
            
            # *three* updates
            if three.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                three.frameNStart = frameN  # exact frame index
                three.tStart = t  # local t and not account for scr refresh
                three.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(three, 'tStartRefresh')  # time at next scr refresh
                three.setAutoDraw(True)
            
            # *four* updates
            if four.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                four.frameNStart = frameN  # exact frame index
                four.tStart = t  # local t and not account for scr refresh
                four.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(four, 'tStartRefresh')  # time at next scr refresh
                four.setAutoDraw(True)
            
            # *five* updates
            if five.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                five.frameNStart = frameN  # exact frame index
                five.tStart = t  # local t and not account for scr refresh
                five.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(five, 'tStartRefresh')  # time at next scr refresh
                five.setAutoDraw(True)
            
            # *instr_feedback* updates
            if instr_feedback.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                instr_feedback.frameNStart = frameN  # exact frame index
                instr_feedback.tStart = t  # local t and not account for scr refresh
                instr_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instr_feedback, 'tStartRefresh')  # time at next scr refresh
                instr_feedback.setAutoDraw(True)
            # *feedback_click* updates
            if feedback_click.status == NOT_STARTED and t >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                feedback_click.frameNStart = frameN  # exact frame index
                feedback_click.tStart = t  # local t and not account for scr refresh
                feedback_click.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_click, 'tStartRefresh')  # time at next scr refresh
                feedback_click.status = STARTED
                feedback_click.mouseClock.reset()
                prevButtonState = feedback_click.getPressed()  # if button is down already this ISN'T a new click
            if feedback_click.status == STARTED:  # only update if started and not finished!
                buttons = feedback_click.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [one,two,three,four,five]:
                            if obj.contains(feedback_click):
                                gotValidClick = True
                                feedback_click.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedback"-------
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for feedback_questions (TrialHandler)
        # Mapping and appending answers
        ans = word2int[feedback_click.clicked_name[0]]
        answers.append((question_id, ans))
        
        # On last question send routine annotation
        if feedback_questions.thisN == 3:
            annot_stop = time_fn()
            duration = annot_stop - annot_start
         
            annot = new_wordset_trigger('feedback', duration, annot_start)
            
            # Add answers to annotation
            for a in answers:
                annot[f'feedback_{a[0]}'] = a[1]
            send_trigger(annot)
            sleep(0.1) 
        # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1.0 repeats of 'feedback_questions'
    
    
    # ------Prepare to start Routine "one_back_begin"-------
    continueRoutine = True
    routineTimer.add(7.750000)
    # update component parameters for each repeat
    print('1-back setup')
    
    # Init. counters to zero
    correct = 0
    total = 0
    
    # Init. letters for oneback
    p = 0.4 # Prob. of "true" stim
    bool_mask = randchoice([True, False], size=(num_one_back),p=[p,1-p])
    
    first_letter = randchoice(letters)
    one_back_stim = []
    
    # Generate letters for oneback
    for i in range(num_one_back): 
        prev_stim = first_letter if i == 0 else one_back_stim[i-1]
        
        if bool_mask[i]:    
            one_back_stim.append(prev_stim)
        else:
            new_stim = randchoice([x for x in letters if x!= prev_stim])
            one_back_stim.append(new_stim)
    one_back_start_letter.setText(first_letter)
    # keep track of which components have finished
    one_back_beginComponents = [one_back_begin_text, one_back_start_letter]
    for thisComponent in one_back_beginComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    one_back_beginClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "one_back_begin"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = one_back_beginClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=one_back_beginClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *one_back_begin_text* updates
        if one_back_begin_text.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            one_back_begin_text.frameNStart = frameN  # exact frame index
            one_back_begin_text.tStart = t  # local t and not account for scr refresh
            one_back_begin_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(one_back_begin_text, 'tStartRefresh')  # time at next scr refresh
            one_back_begin_text.setAutoDraw(True)
        if one_back_begin_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > one_back_begin_text.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                one_back_begin_text.tStop = t  # not accounting for scr refresh
                one_back_begin_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(one_back_begin_text, 'tStopRefresh')  # time at next scr refresh
                one_back_begin_text.setAutoDraw(False)
        
        # *one_back_start_letter* updates
        if one_back_start_letter.status == NOT_STARTED and tThisFlip >= 5.75-frameTolerance:
            # keep track of start time/frame for later
            one_back_start_letter.frameNStart = frameN  # exact frame index
            one_back_start_letter.tStart = t  # local t and not account for scr refresh
            one_back_start_letter.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(one_back_start_letter, 'tStartRefresh')  # time at next scr refresh
            one_back_start_letter.setAutoDraw(True)
        if one_back_start_letter.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > one_back_start_letter.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                one_back_start_letter.tStop = t  # not accounting for scr refresh
                one_back_start_letter.frameNStop = frameN  # exact frame index
                win.timeOnFlip(one_back_start_letter, 'tStopRefresh')  # time at next scr refresh
                one_back_start_letter.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in one_back_beginComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "one_back_begin"-------
    for thisComponent in one_back_beginComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Begin timer after first_letter
    one_back_timer = core.CountdownTimer(22)
    
    annot_start = time_fn()
    
    # set up handler to look after randomisation of conditions etc
    one_back_loop_two = data.TrialHandler(nReps=num_one_back, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='one_back_loop_two')
    thisExp.addLoop(one_back_loop_two)  # add the loop to the experiment
    thisOne_back_loop_two = one_back_loop_two.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisOne_back_loop_two.rgb)
    if thisOne_back_loop_two != None:
        for paramName in thisOne_back_loop_two:
            exec('{} = thisOne_back_loop_two[paramName]'.format(paramName))
    
    for thisOne_back_loop_two in one_back_loop_two:
        currentLoop = one_back_loop_two
        # abbreviate parameter names if possible (e.g. rgb = thisOne_back_loop_two.rgb)
        if thisOne_back_loop_two != None:
            for paramName in thisOne_back_loop_two:
                exec('{} = thisOne_back_loop_two[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "one_back"-------
        continueRoutine = True
        # update component parameters for each repeat
        # Set n to current iter in one-back loop
        n = currentLoop.thisN
        
        # Init stims.
        curr_stim = one_back_stim[n]
        prev_stim = first_letter if n == 0 else one_back_stim[n-1]
        
        
        
        stim_text.setText(curr_stim)
        # keep track of which components have finished
        one_backComponents = [stim_text]
        for thisComponent in one_backComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        one_backClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "one_back"-------
        while continueRoutine:
            # get current time
            t = one_backClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=one_backClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Stop when one-back task timer is up
            if one_back_timer.getTime() < 0: 
                # Send one-back routine annotations
                annot_stop = time_fn()
                duration = annot_stop - annot_start
                
                annot = new_trigger('oneback', duration, annot_start)
                annot['problem_id'] = problem_id
                annot['oneback_correct'] = correct
                annot['oneback_total'] = total
                annot['oneback_score'] = correct/total
                send_trigger(annot)
                sleep(0.1) 
               
                continueRoutine = False
                currentLoop.finished = True
                    
            # Max 2 seconds per letter
            if one_backClock.getTime() >= 2.0:
                if not bool_mask[n]: #curr_stim != prev_stim:
                    correct += 1
                    total += 1 
                else:
                    total += 1
                
                continueRoutine = False
            
            # Check for space key press (and right for skip)
            press_time = one_backClock.getTime()
            pressed_keys = defaultKeyboard.getKeys(['space', 'right'])
            
            if 'space' in pressed_keys and press_time >= 0.25:
                if bool_mask[n]: #curr_stim == prev_stim:
                    # Add only reaction time for correct "pushes"
                    reaction_time = press_time - 0.25 #due to 0.25 delay
                   
                    # Send annotation with reaction time
                    annot = new_trigger('oneback_reaction')
                    annot['problem_id'] = problem_id
                    annot['oneback_reactiontime'] = reaction_time
                    send_trigger(annot)
                    sleep(0.05) 
            
                    correct += 1
                    total += 1 
                else: 
                    total += 1
                    
                continueRoutine = False
             
            # For skipping
            if 'right' in pressed_keys:
                continueRoutine = False
                currentLoop.finished = True
            
            # *stim_text* updates
            if stim_text.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
                # keep track of start time/frame for later
                stim_text.frameNStart = frameN  # exact frame index
                stim_text.tStart = t  # local t and not account for scr refresh
                stim_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_text, 'tStartRefresh')  # time at next scr refresh
                stim_text.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in one_backComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "one_back"-------
        for thisComponent in one_backComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "one_back" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed num_one_back repeats of 'one_back_loop_two'
    
    
    # ------Prepare to start Routine "save_rec"-------
    continueRoutine = True
    # update component parameters for each repeat
    # Save files in case of delay due 
    if mic_on:
        # File names for recording of each wordset
        mic_filename_1 = recordingDir + fr'\participant_{participant_id}_problem{problem_id}_{stimuli}_wordset1.wav'
        mic_filename_2 = recordingDir + fr'\participant_{participant_id}_problem{problem_id}_{stimuli}_wordset2.wav'
        
        # Save both recordings
        wav_write(mic_filename_1, fs, mic_recording_1)
        wav_write(mic_filename_2, fs, mic_recording_2)
    
    # keep track of which components have finished
    save_recComponents = []
    for thisComponent in save_recComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    save_recClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "save_rec"-------
    while continueRoutine:
        # get current time
        t = save_recClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=save_recClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in save_recComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "save_rec"-------
    for thisComponent in save_recComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "save_rec" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'design_problems'


# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# Set time and convert to time for text
total_seconds = time_fn()
time_string = str(datetime.timedelta(seconds=int(total_seconds)))

print('Exp. over')

# Send routine annotation
annot = new_trigger('experiment over', timestamp=total_seconds)
send_trigger(annot)
sleep(0.1) 

thanks_text.setText('Thank you for taking part in the experiment!')
time_text.setText(f'Total time: {time_string}')
# keep track of which components have finished
thanksComponents = [thanks_text, time_text]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks_text* updates
    if thanks_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks_text.frameNStart = frameN  # exact frame index
        thanks_text.tStart = t  # local t and not account for scr refresh
        thanks_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks_text, 'tStartRefresh')  # time at next scr refresh
        thanks_text.setAutoDraw(True)
    if thanks_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thanks_text.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            thanks_text.tStop = t  # not accounting for scr refresh
            thanks_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thanks_text, 'tStopRefresh')  # time at next scr refresh
            thanks_text.setAutoDraw(False)
    
    # *time_text* updates
    if time_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        time_text.frameNStart = frameN  # exact frame index
        time_text.tStart = t  # local t and not account for scr refresh
        time_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(time_text, 'tStartRefresh')  # time at next scr refresh
        time_text.setAutoDraw(True)
    if time_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > time_text.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            time_text.tStop = t  # not accounting for scr refresh
            time_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(time_text, 'tStopRefresh')  # time at next scr refresh
            time_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Stop Pupil recording
pupil_remote.send_string("r")
pupil_remote.recv_string()
sleep(0.1)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
