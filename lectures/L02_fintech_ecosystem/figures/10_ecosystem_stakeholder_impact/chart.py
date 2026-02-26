"""
Figure 10: Ecosystem Stakeholder Impact
Radar/spider chart comparing 6 stakeholders across 5 dimensions.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '_shared'))

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
    'title': 'Ecosystem Stakeholder Impact',
    'type': 'radar',
    'section': 'Stakeholder Analysis',
    'lecture_number': 2,
}

dimensions = ['Access', 'Cost\nReduction', 'Innovation', 'Risk', 'Regulatory\nBurden']
N = len(dimensions)

stakeholders = {
    'Consumers':      [8, 7, 8, 5, 2],
    'Banks':          [3, 4, 6, 7, 8],
    'Fintechs':       [7, 6, 9, 8, 6],
    'Regulators':     [5, 3, 4, 9, 10],
    'Investors':      [4, 3, 8, 7, 3],
    'Tech Providers': [6, 5, 9, 4, 2],
}

colors = [V4_COLORS['MLGREEN'], V4_COLORS['MLBLUE'], V4_COLORS['MLORANGE'],
          V4_COLORS['MLRED'], V4_COLORS['MLPURPLE'], V4_COLORS['MLCYAN']]

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]  # Close the polygon

fig, ax = plt.subplots(1, 1, figsize=(10, 6), subplot_kw=dict(polar=True))
fig.patch.set_facecolor('white')

for (name, values), color in zip(stakeholders.items(), colors):
    vals = values + values[:1]  # Close
    ax.plot(angles, vals, 'o-', linewidth=2, color=color, label=name, markersize=4)
    ax.fill(angles, vals, alpha=0.15, color=color)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(dimensions, fontsize=9, color='#555555')
ax.set_ylim(0, 10)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], fontsize=7, color='#888888')
ax.set_rlabel_position(30)

# Grid styling
ax.grid(color='#DDDDDD', linewidth=0.5)
ax.spines['polar'].set_color('#CCCCCC')

ax.set_title('Ecosystem Stakeholder Impact Analysis',
             fontsize=14, fontweight='bold', pad=25, color='#333333')

ax.legend(loc='center left', bbox_to_anchor=(1.15, 0.5), fontsize=9,
          frameon=True, facecolor='white', edgecolor='#CCCCCC')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
