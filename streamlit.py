import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.ndimage.filters import gaussian_filter
import streamlit as st


# Assume one session and one export per participant
filepath = f'../Experiment/Data/Pupil data/test_heatmap/000/exports/001/' 
w,h = 1920,1200


@st.cache
def read_df():
    surface_gaze = pd.read_csv(filepath+'surfaces/gaze_positions_on_surface_Monitor.csv')
    surface_gaze = surface_gaze[surface_gaze['on_surf'] == True]

    return surface_gaze

@st.cache
def gen_heatmap(data, blur):
    # Ensure square bins
    num_bins = 50
    bins = (num_bins, int(num_bins / (w/h)))

    x, y = data['x_scaled'], data['y_scaled']

    # ax.hist2d(x,y, bins=bins, range=[[0,w],[0,h]], alpha=0.8, zorder=1)
    heatmap, _, _ = np.histogram2d(x, y, bins=bins, range=[[0,w],[0,h]])

    if blur:
        heatmap = gaussian_filter(heatmap, sigma=1)

    return heatmap

def draw_heatmap(heatmap):
    # Plot heatmaps
    fig, ax = plt.subplots()

    extent = [0,w,0,h] 
    ax.imshow(heatmap.T,extent=extent, origin='lower', cmap='viridis', alpha=0.5, zorder=1)
    ax.imshow(np.flipud(plt.imread('wordset2.png')), origin='lower', zorder=0)

    ax.axis('off')

    return fig

###############

st.sidebar.button('Hit me!')
st.sidebar.selectbox('Problem', list((range(1,13))))
st.sidebar.radio('Wordset', [1,2])
st.sidebar.selectbox('Participant', [f'{id:03}' for id in range(1,24)])

st.title('Design Ideation dataset')

loading_df_state = st.text('Loading data...')
data = read_df()
st.write("## Gaze data on surface", data.head(100))
loading_df_state.text('Loading data... Done!')

st.markdown('## Heatmap')
blur = st.checkbox('Blurred heatmap?')

heatmap = gen_heatmap(data,blur)
fig = draw_heatmap(heatmap)
st.write(fig)



