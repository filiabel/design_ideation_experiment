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

LSL offers great functionality for syncing hardware and software when conducting research experiments. Standalone PsychoPy has the Python interface [pylsl](https://github.com/labstreaminglayer/liblsl-Python) installed by default. `LSL_code.py` showcases an example on how to implement LSL into PsychoPy for annotations. LSL was not used in this experiment, as Pupil Network API offered similar functionality for this use case.

LSL interfaces:
* [LabRecorder](https://github.com/labstreaminglayer/App-LabRecorder) - client to choose streams from the network and save to .xdf file.
* [Pupil Capture LSL Relay](https://github.com/labstreaminglayer/App-PupilLabs/blob/master/pupil_capture/README.md) - plugin to send data from Pupil to the LSL stream.
* [Collection of apps and tools for LabStreamingLayer](https://github.com/labstreaminglayer/)
