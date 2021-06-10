# Design Ideation Experiment
This repository contains the work related to my Master Thesis at TrollLABS NTNU, spring 2021.

The experimental setup is based on the following research paper:
> Goucher-Lambert, K., Moss, J., & Cagan, J. (2019). A neuroimaging investigation of design ideation with and without inspirational stimuli — Understanding the meaning of near and far stimuli. Design Studies, 60, 1–38. https://doi.org/10.1016/j.destud.2018.07.001


## Repository Structure
* The experiment itself and other related files related to PsychoPy are stored in [this folder](Psyhopy/psychopy.md). It also contains snippet of useful codes used in custom code components throughout the experiment. E.g. communication with Pupil Capture software and 
  * Previous versions of the PsychoPy experiment is also included. One which annotates the experiment timeline using LabStreamingLayer (LSL). Some components may differ from the final experiment.
* Code used for data preprocessing and analysis can be found in [this folder](Data analysis/data_analysis.md). Some it also contains a helper function for writing LSL streams saved in .xdf format to .csv. 
