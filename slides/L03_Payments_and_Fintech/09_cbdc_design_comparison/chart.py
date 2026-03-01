"""
Figure 09: CBDC Design Comparison
Matrix/heatmap comparing CBDC design dimensions: Retail vs. Wholesale
on axes of Privacy, Programmability, Intermediation, Offline Capability.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '_shared'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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
    'title': 'CBDC Design Comparison Matrix',
    'type': 'comparison_bar',
    'section': 'CBDCs and Digital Currency',
    'lecture_number': 3,
}

np.random.seed(42)

# Design dimensions (rows) and CBDC types (columns)
dimensions = ['Privacy', 'Programmability', 'Intermediation', 'Offline\nCapability',
              'Scalability', 'Interoperability']
cbdc_types = ['Retail\nCBDC', 'Wholesale\nCBDC', 'Hybrid\nCBDC']

# ILLUSTRATIVE scores (1=Low, 2=Medium, 3=High)
# Rows: dimensions, Columns: cbdc_types
scores = np.array([
    [2, 3, 2],   # Privacy
    [2, 3, 3],   # Programmability
    [3, 1, 2],   # Intermediation (retail needs more intermediaries)
    [3, 1, 2],   # Offline Capability
    [2, 3, 3],   # Scalability
    [2, 2, 3],   # Interoperability
])

labels_map = {1: 'Low', 2: 'Medium', 3: 'High'}
color_map = {
    1: V4_COLORS['MLRED'],
    2: V4_COLORS['MLORANGE'],
    3: V4_COLORS['MLTEAL'],
}

fig, ax = plt.subplots(1, 1, figsize=(10, 6))

# Draw heatmap manually for better control
cell_w, cell_h = 1.0, 1.0

for i, dim in enumerate(dimensions):
    for j, ctype in enumerate(cbdc_types):
        score = scores[i, j]
        color = color_map[score]
        rect = mpatches.FancyBboxPatch(
            (j * cell_w + 2.5, (len(dimensions) - 1 - i) * cell_h + 0.5),
            cell_w - 0.08, cell_h - 0.08,
            boxstyle="round,pad=0.05",
            facecolor=color, edgecolor='white', linewidth=2, alpha=0.75)
        ax.add_patch(rect)
        ax.text(j * cell_w + 2.5 + (cell_w - 0.08) / 2,
                (len(dimensions) - 1 - i) * cell_h + 0.5 + (cell_h - 0.08) / 2,
                labels_map[score], ha='center', va='center',
                fontsize=10, fontweight='bold', color='white')

# Row labels (dimensions)
for i, dim in enumerate(dimensions):
    ax.text(2.3, (len(dimensions) - 1 - i) * cell_h + 0.5 + (cell_h - 0.08) / 2,
            dim, ha='right', va='center', fontsize=9, fontweight='bold', color='#444444')

# Column labels (CBDC types)
for j, ctype in enumerate(cbdc_types):
    ax.text(j * cell_w + 2.5 + (cell_w - 0.08) / 2,
            len(dimensions) * cell_h + 0.65,
            ctype, ha='center', va='center',
            fontsize=10, fontweight='bold', color='#333333')

# Legend
legend_patches = [
    mpatches.Patch(facecolor=color_map[3], edgecolor='white', label='High'),
    mpatches.Patch(facecolor=color_map[2], edgecolor='white', label='Medium'),
    mpatches.Patch(facecolor=color_map[1], edgecolor='white', label='Low'),
]
ax.legend(handles=legend_patches, loc='lower right', fontsize=9,
          frameon=True, framealpha=0.9, edgecolor='#CCCCCC', title='Score',
          title_fontsize=9)

ax.set_xlim(0, 6.5)
ax.set_ylim(-0.2, len(dimensions) * cell_h + 1.5)
ax.axis('off')

ax.set_title('CBDC Design Comparison Matrix (Illustrative)',
             fontsize=14, fontweight='bold', pad=15, color='#333333')

fig.text(0.5, 0.01,
         'Scores are illustrative. Actual designs vary by jurisdiction.',
         ha='center', fontsize=7, fontstyle='italic', color='#999999')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
