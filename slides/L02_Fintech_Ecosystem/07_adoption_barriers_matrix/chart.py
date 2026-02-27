"""
Figure 07: Adoption Barriers Matrix
Heatmap of barrier intensity across demographics.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '_shared'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
import numpy as np

try:
    from chart_styles import V4_COLORS, apply_v4_style, save_chart
except ImportError:
    V4_COLORS = {
        'MLPURPLE': '#9467BD', 'MLBLUE': '#1F77B4', 'MLRED': '#D62728',
        'MLORANGE': '#FF7F0E', 'MLGREEN': '#2CA02C', 'MLGRAY': '#7F7F7F',
        'MLTEAL': '#0D7377', 'MLCYAN': '#14BDEB', 'MLYELLOW': '#BCBD22',
        'MLPINK': '#E377C2', 'MLBROWN': '#8C564B',
    }
    def apply_v4_style(ax, title='', xlabel='', ylabel=''):
        ax.set_title(title, fontsize=14, fontweight='bold', pad=15, color='#333333')
        if xlabel: ax.set_xlabel(xlabel, fontsize=11, color='#555555')
        if ylabel: ax.set_ylabel(ylabel, fontsize=11, color='#555555')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#CCCCCC')
        ax.spines['bottom'].set_color('#CCCCCC')
        ax.tick_params(colors='#555555', labelsize=9)
        ax.set_facecolor('white')
        return ax
    def save_chart(fig, filename='chart.pdf', dpi=300):
        fig.tight_layout()
        fig.savefig(filename, format='pdf', bbox_inches='tight', dpi=dpi, facecolor='white')
        plt.close(fig)
        print(f'Saved: {filename}')

CHART_METADATA = {
    'title': 'Adoption Barriers Matrix',
    'type': 'heatmap',
    'section': 'Barriers to Adoption',
    'lecture_number': 2,
}

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
fig.patch.set_facecolor('white')

barriers = ['Trust Deficit', 'Complexity', 'Cost Sensitivity',
            'Digital Literacy', 'Regulatory Friction', 'Infrastructure Gap']
demographics = ['Gen Z', 'Millennial', 'Gen X', 'Boomer', 'Rural', 'Low-Income']

data = np.array([
    [2, 2, 3, 4, 4, 3],  # Trust
    [1, 1, 2, 4, 3, 3],  # Complexity
    [2, 2, 2, 2, 4, 5],  # Cost
    [1, 1, 2, 3, 4, 4],  # Digital Literacy
    [1, 2, 3, 4, 2, 2],  # Regulatory
    [1, 1, 1, 1, 5, 4],  # Infrastructure
])

# Green -> Yellow -> Red colormap
cmap = mcolors.LinearSegmentedColormap.from_list('barrier',
    ['#2CA02C', '#BCBD22', '#FF7F0E', '#D62728'], N=256)

im = ax.imshow(data, cmap=cmap, aspect='auto', vmin=1, vmax=5)

# Number annotations in cells
for i in range(len(barriers)):
    for j in range(len(demographics)):
        val = data[i, j]
        text_color = 'white' if val >= 4 else '#333333'
        ax.text(j, i, str(val), ha='center', va='center',
                fontsize=13, fontweight='bold', color=text_color)

ax.set_xticks(range(len(demographics)))
ax.set_xticklabels(demographics, fontsize=10, rotation=0)
ax.set_yticks(range(len(barriers)))
ax.set_yticklabels(barriers, fontsize=10)

# Colorbar
cbar = plt.colorbar(im, ax=ax, shrink=0.8, pad=0.02)
cbar.set_label('Barrier Intensity', fontsize=10, color='#555555')
cbar.set_ticks([1, 2, 3, 4, 5])
cbar.set_ticklabels(['1\nLow', '2', '3\nMedium', '4', '5\nHigh'])
cbar.ax.tick_params(labelsize=8, colors='#555555')

ax.set_title('Adoption Barriers by Demographic',
             fontsize=14, fontweight='bold', pad=15, color='#333333')

# Remove default spines for heatmap
for spine in ax.spines.values():
    spine.set_visible(False)

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
