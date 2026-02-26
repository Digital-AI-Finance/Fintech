"""
Figure 03: Collaboration Models Matrix
Grouped horizontal bar chart: 4 models x 5 dimensions on 1-5 scale.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '_shared'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
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
    'title': 'Collaboration Models Comparison',
    'type': 'comparison_bar',
    'section': 'HOW',
    'lecture_number': 1,
}

# Models and dimensions
models = ['Partnership', 'Acquisition', 'White-Label', 'Open Banking']
dimensions = ['Control', 'Speed-to-Market', 'Cost Efficiency', 'Innovation\nPotential', 'Risk Level']

# Illustrative ratings (rows = dimensions, cols = models): scale 1-5
# Partnership: med control, high speed, med cost, high innovation, med risk
# Acquisition: high control, low speed, low cost-eff, med innovation, high risk
# White-Label: med-low control, high speed, high cost-eff, med innovation, low risk
# Open Banking: low control, med speed, high cost-eff, very high innovation, low risk
ratings = np.array([
    [3, 5, 2, 2],   # Control
    [4, 2, 4, 3],   # Speed-to-Market
    [3, 1, 4, 5],   # Cost Efficiency
    [4, 3, 3, 5],   # Innovation Potential
    [3, 4, 2, 2],   # Risk Level
])

colors = [V4_COLORS['MLTEAL'], V4_COLORS['MLPURPLE'],
          V4_COLORS['MLORANGE'], V4_COLORS['MLBLUE']]

n_dims = len(dimensions)
n_models = len(models)
group_height = 0.18
offsets = np.array([-(n_models - 1) / 2 + i for i in range(n_models)]) * group_height

fig, ax = plt.subplots(figsize=(10, 6))

y_positions = np.arange(n_dims)

for m_idx, (model, color) in enumerate(zip(models, colors)):
    vals = ratings[:, m_idx]
    y = y_positions + offsets[m_idx]
    bars = ax.barh(y, vals, height=group_height * 0.9,
                   color=color, alpha=0.85, label=model)
    for bar, val in zip(bars, vals):
        ax.text(val + 0.05, bar.get_y() + bar.get_height() / 2,
                str(val), va='center', ha='left', fontsize=7.5, color='#555555')

apply_v4_style(ax,
               title='Bank\u2013Fintech Collaboration Models: Comparative Analysis',
               xlabel='Score (1 = Low, 5 = High)',
               ylabel='')

ax.set_yticks(y_positions)
ax.set_yticklabels(dimensions, fontsize=10)
ax.set_xlim(0, 6.2)
ax.set_xticks([1, 2, 3, 4, 5])
ax.axvline(x=1, color='#EEEEEE', linewidth=0.8, zorder=0)
ax.axvline(x=2, color='#EEEEEE', linewidth=0.8, zorder=0)
ax.axvline(x=3, color='#EEEEEE', linewidth=0.8, zorder=0)
ax.axvline(x=4, color='#EEEEEE', linewidth=0.8, zorder=0)
ax.axvline(x=5, color='#EEEEEE', linewidth=0.8, zorder=0)

ax.legend(loc='lower right', fontsize=9, framealpha=0.9,
          title='Collaboration Model', title_fontsize=9)

ax.text(0.01, -0.07, 'Illustrative ratings \u2014 conceptual comparison only.',
        transform=ax.transAxes, fontsize=7.5, color='#888888', style='italic')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
