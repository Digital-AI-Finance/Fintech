"""
Figure 06: Global Regulatory Comparison Matrix
Heatmap-style comparison of 6 jurisdictions across 5 regulatory dimensions
with color gradient cells scored 1-5.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '_shared'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap
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
    'title': 'Global Regulatory Comparison Matrix',
    'type': 'comparison_bar',
    'section': 'Regulatory Landscape',
    'lecture_number': 4,
}

np.random.seed(42)

jurisdictions = ['US', 'EU', 'UK', 'Singapore', 'Switzerland', 'China']
dimensions = ['Sandbox\nAvailability', 'Crypto\nFramework', 'Open Banking\nMandate',
              'AML\nRigor', 'Licensing\nSpeed']

# Illustrative scores (1-5)
scores = np.array([
    [2, 3, 2, 5, 2],  # US
    [4, 4, 5, 5, 3],  # EU
    [5, 4, 5, 4, 4],  # UK
    [5, 4, 3, 4, 5],  # Singapore
    [3, 5, 3, 5, 4],  # Switzerland
    [1, 2, 1, 4, 3],  # China
])

# Custom colormap: red (1) -> yellow (3) -> green (5)
cmap = LinearSegmentedColormap.from_list('reg',
    [(0.0, '#D62728'), (0.25, '#FF7F0E'), (0.5, '#BCBD22'),
     (0.75, '#2CA02C'), (1.0, '#0D7377')])

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
fig.patch.set_facecolor('white')

im = ax.imshow(scores, cmap=cmap, vmin=1, vmax=5, aspect='auto')

# Annotate cells with scores
for i in range(len(jurisdictions)):
    for j in range(len(dimensions)):
        val = scores[i, j]
        text_color = 'white' if val <= 2 or val >= 4 else '#333333'
        ax.text(j, i, str(val), ha='center', va='center',
                fontsize=14, fontweight='bold', color=text_color)

ax.set_xticks(np.arange(len(dimensions)))
ax.set_xticklabels(dimensions, fontsize=9, fontweight='bold', color='#555555')
ax.set_yticks(np.arange(len(jurisdictions)))
ax.set_yticklabels(jurisdictions, fontsize=10, fontweight='bold', color='#555555')

ax.set_xticks(np.arange(len(dimensions) + 1) - 0.5, minor=True)
ax.set_yticks(np.arange(len(jurisdictions) + 1) - 0.5, minor=True)
ax.grid(which='minor', color='white', linewidth=2)
ax.tick_params(which='minor', bottom=False, left=False)

# Colorbar
cbar = fig.colorbar(im, ax=ax, shrink=0.7, pad=0.02)
cbar.set_ticks([1, 2, 3, 4, 5])
cbar.set_ticklabels(['1\nWeak', '2', '3\nModerate', '4', '5\nStrong'])
cbar.ax.tick_params(labelsize=8, colors='#555555')

for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_title('Global Fintech Regulatory Comparison',
             fontsize=14, fontweight='bold', pad=15, color='#333333')

ax.text(2.0, 6.8, 'Illustrative scores (1 = Weak/Absent, 5 = Strong/Comprehensive)',
        ha='center', va='center', fontsize=8, color='#888888',
        fontstyle='italic', transform=ax.transData)

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
