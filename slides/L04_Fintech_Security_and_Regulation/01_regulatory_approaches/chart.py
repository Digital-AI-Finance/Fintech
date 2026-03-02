"""
Figure 01: Regulatory Approaches Comparison
Grouped bar chart comparing 5 countries across 5 regulatory dimensions
with illustrative scores from 1-5, color-coded by dimension.
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
    'title': 'Regulatory Approaches Comparison',
    'type': 'comparison_bar',
    'section': 'Regulatory Landscape',
    'lecture_number': 4,
}

np.random.seed(42)

countries = ['US', 'EU', 'UK', 'Singapore', 'China']
dimensions = ['Innovation\nSpeed', 'Consumer\nProtection', 'Compliance\nEase',
              'Market\nCompetition', 'Systemic Risk\nControl']

# Illustrative scores (1-5)
scores = np.array([
    [4, 3, 2, 4, 3],  # US
    [3, 5, 3, 4, 4],  # EU
    [5, 4, 4, 5, 3],  # UK
    [5, 4, 5, 4, 4],  # Singapore
    [2, 3, 2, 2, 5],  # China
])

dim_colors = [
    V4_COLORS['MLBLUE'], V4_COLORS['MLGREEN'], V4_COLORS['MLORANGE'],
    V4_COLORS['MLPURPLE'], V4_COLORS['MLRED'],
]

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
fig.patch.set_facecolor('white')

x = np.arange(len(countries))
n_dims = len(dimensions)
bar_width = 0.15
offsets = np.arange(n_dims) - (n_dims - 1) / 2

for i, (dim, color) in enumerate(zip(dimensions, dim_colors)):
    positions = x + offsets[i] * bar_width
    bars = ax.bar(positions, scores[:, i], bar_width, label=dim,
                  color=color, alpha=0.85, edgecolor='white', linewidth=0.5)
    for bar, val in zip(bars, scores[:, i]):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1,
                str(val), ha='center', va='bottom', fontsize=7, color='#555555',
                fontweight='bold')

ax.set_xticks(x)
ax.set_xticklabels(countries, fontsize=10, fontweight='bold')
ax.set_ylim(0, 6.2)
ax.set_yticks([1, 2, 3, 4, 5])
ax.yaxis.grid(True, alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

apply_v4_style(ax, title='Regulatory Approaches: Cross-Country Comparison',
               ylabel='Score (1 = Low, 5 = High)')

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08), ncol=5,
          fontsize=8, frameon=False)

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
