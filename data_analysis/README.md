# Data Analysis
This folder includes code for analyzing eye-tracking data from Pupil Capture, as well as general statistics and plotting done for the processed data.

Notebooks are presented as is, but can showcase how to analyze the data. Using Pandas functionality such as boolean indexing like `gaze[gaze.participant_id == 1]` for selectingf data subsets and group by like `gaze.groupby(by=['stimuli'])` for grouping selections and then using reucing methods such as `mean()`. 

Screenshot of each unique wordset routine is included in folder `images`. This can be useful for plotting heatmaps, scanpath or other visualizations above the stimuli for context. 

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
_Fixation scanpath for participant 006 across all problems on wordset 2. Light to dark line indicate temporality, and scatter point size indicates fixation duration._
![Scanpath](https://i.imgur.com/63n1vDd.png)

#### Code
```python
def plot_scanpath(ax, x, y, duration):
  N = len(x) # Number of fixations
  
  # Plotting each segment at the time to adjust for alpha values.
  # This enables us to read out temporality from the plot (low opacity --> high opacity)
  for i in range(N):
    alpha = 0.15 + 0.8*(i/N)
    polyline = ax.plot(x[i:i+2], y[i:i+2], "C3", lw=1, alpha=alpha, solid_capstyle='round')
    points = ax.scatter(x[i], y[i], s=duration[i]/10, alpha=alpha-0.1, color='blue')
  
  # Plots in place on Axis ax. See notebook for use of function.
```
