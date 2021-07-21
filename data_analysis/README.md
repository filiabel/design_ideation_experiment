# Data Analysis
This folder includes code for analyzing eye-tracking data from Pupil Capture, as well as general statistics and plotting done for the processed data.

Notebooks are presented as is, but can showcase how to analyze the data. Using Pandas functionality such as boolean indexing like `gaze[gaze.participant_id == 1]` for selectingf data subsets and group by like `gaze.groupby(by=['stimuli'])` for grouping selections and then using reucing methods such as `mean()`. 

Screenshot of each unique wordset routine is included in folder `images`. This can be useful for plotting heatmaps, scanpath or other visualizations above the stimuli for context. 

## Transcription analysis
Using Python library `SpaCy`, all transcriptions were run through their text processing pipeline. By extracting the lemma (root word) of each word, and removing stop words etc., one can find the most frequent words across all problem/wordset/stimuli combinations. 

After this, the intersection of words across all stimuli within a problem/wordset was calculated to see which words (and thus ideas, in a way) were prevalent indepent of stimuli.

## Visualization examples
### Heatmaps
_Aggregated heatmaps across stimuli and wordset for all participants._
![Heatmaps](https://i.imgur.com/bQvHeDH.png)

#### Code
```python
def generate_heatmap(x, y, bins=(w,h), blur=0.04,thres=True):
  '''
  blur - this will determine the gaussian blur kernel of the image (higher number = more blur). 
    blur == 0.04 gives Gaussian kernel sd values of respectively 77 and 49 for width and height.

  Based on: https://github.com/pupil-labs/pupil-tutorials/blob/master/02_load_exported_surfaces_and_visualize_aggregate_heatmap.ipynb
  '''
  # 2D histogram
  heatmap, xedges, yedges = np.histogram2d(x, y, bins=bins, range=[[0,w],[0,h]])
  
  # Gaussian blur  
  if blur:
    filter_w = int(blur * w) // 2 * 2 + 1
    filter_h = int(blur * h) // 2 * 2 + 1
  
    heatmap = gaussian_filter(heatmap, sigma=(filter_w, filter_h))

  # Thresholding
  if thres:
    lowbound = np.mean(heatmap[heatmap > 0]) / 2
    heatmap[heatmap < lowbound] = np.nan

  return heatmap # plot using imshow, see notebook.
```

### Scanpaths
_Fixation scanpath for participant 006 across all problems on wordset 2. Opacity indicates temporality, and scatter point size indicates fixation duration. The scanpath start point is marked in green, and the end in cyan._
![Scanpath](https://i.imgur.com/v0oRouV.png)

#### Code
```python
def plot_scanpath(ax, x, y, duration):
    N = len(duration)

    # Arbitrary value to mark size of end points on scanpaths
    size_ends = np.mean(duration) / 3

    for i in range(N):
      alpha = 0.15 + 0.70*(i/N) # Alpha gradually decreasing as "time" goes by.
      
      # Plot one line segment
      polyline = ax.plot(x[i:i+2], y[i:i+2], "C3", lw=1, alpha=alpha, solid_capstyle='round', zorder=i+1)
      
      # Add color for beginning and end in green and cyan, respectively. 
      # zorder ensures correct layer with scatter on top.
      if i == 0:
        points = ax.scatter(x[i], y[i], s=size_ends, alpha=0.85, color='lime',zorder=i+2)
      elif i == N-1:
        points = ax.scatter(x[i], y[i], s=size_ends, alpha=0.85, color='cyan',zorder=i+2)
      else:
        points = ax.scatter(x[i], y[i], s=duration[i]/10, alpha=alpha-0.1, color='blue',zorder=i+2)
  
  # Plots in place on Axis ax. See notebook for use of function.
```
