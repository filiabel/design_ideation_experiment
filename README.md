# Design Ideation Experiment
This repository contains the work related to my Master Thesis at [TrollLABS](https://www.ntnu.edu/mtp/trolllabs), spring 2021.

Design ideation study using eye tracking technology (N = 24). Participants receive open ended design problems and a set of words on the monitor,  and the words are ment to serve as inspirational stimuli for solving the design problems at hand. Their job is to generate as many ideas as possible for each design problem. During the ideation, the participants are to speak out loud and gets recorded.

The entire experimental setup is made using open-source software, mainly [PsychoPy](https://psychopy.org/) and [Pupil Core](https://pupil-labs.com/products/core/), and is therefore _**reproducible by anyone**_. Experimental setup is based on the following research paper:
> Goucher-Lambert, K., Moss, J., & Cagan, J. (2019). A neuroimaging investigation of design ideation with and without inspirational stimuli — Understanding the meaning of near and far stimuli. Design Studies, 60, 1–38. https://doi.org/10.1016/j.destud.2018.07.001

## Dataset
* Processed data wil be made publicly available here: https://doi.org/10.18710/PZQC4A
* Raw export data for each participant and raw data from Pupil Capture will be publicly available here: ___


## Repository Structure
### [Psychopy](psychopy/README.md) 
This folder contains the experiment itself and other related files related to running the PsychoPy experiment.

* PsychoPy version 2021.1.4 (Standalone) was used to build and run the experiment. All necessary Python libraries should be installed by default with the Standalone PsychoPy software (e.g. `zmq` for Pupil Network API and `sounddevice` for audio recording).
* Contains a folder with snippets of useful scripts/code used in PsychoPy's code components throughout the experiment. E.g. communication with Pupil Capture software and sound capture.
  * Code to show how to use LabStreamingLayer (LSL) in the PsychoPy experiment is also included. This can be useful to implement if one are to recreate the experiment with additional biosensors (e.g. EEG, fMRI) in tandem with eye tracking. Pupil Core also supports LSL. 

### [Data Analysis](data_analysis/README.md)
This folder contains data for all eye tracking analysis, experiment statistics and plotting in Jupyter notebooks and normal Python scripts.

### [Data Processing](data_processing/README.md)
This folder contains code used for concatenating all raw data files to managable data and code for transcription of audio recordings.
* Script for writing LSL streams saved in .xdf format to .csv. This was not used in the experiment, as communcation was done with Pupil Network API.

## Environment
`environment.yml` contains all requirements to do data processing and analysis. It can be installed using `conda env create -f environment.yml` in Anaconda prompt.

## Video of experiment
_Press image below to watch a full run of the design ideation experiment._

<a href="http://www.youtube.com/watch?feature=player_embedded&v=xrr0F1UxRKA
" target="_blank"><img src="https://i.imgur.com/JMAxnap.png"
alt="Design Ideation Experiment" width="640" height="360" border="0" /></a>

## Contact
Please contact me at filip (at) abelson.no if you have any further questions. I'd be happy to help with both the dataset and existing codebase.
