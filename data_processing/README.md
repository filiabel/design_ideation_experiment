# Data processing
This folder contains code used to concatenate raw data exported from Pupil Player into more managable data. Some columns from the raw data were dropped, as they played no significance in the further data processing. \
The scripts are written to be run in an interactive Jupyter window, but should run as a normal script as well.

The different scripts creates the following files:
* `export_annotations.py`
  * `all_annotations.csv` - Concatenates all annotation files. This file is used further on for mapping out the different experimental routines.
  * `feedback.csv` - Subset of `all_annotations.csv` containing only the questionnaire feedback for each problem. Also includes a column with the number of ideas generated in during the both wordset routines for the problem.
* `export_[blinks,fixations,gaze,pupillometry].py`
  * `all_*.csv/h5` - Concatenates all files of given type. Using HDF (.h5) for better compression on the larger datasets.
  * `annotated_*.csv/h5` - Subset of the `all_*.csv/h5` file containing only the data from the wordset routines, meaning the data during design ideation. Data is annotated with participant/experiment information from `all_annotations.csv`, so that one easily can mask out the wanted data. `idea_total` contains the number of ideas generated in the associated wordset routine.
