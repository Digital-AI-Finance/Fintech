"""
Figure 09: Compliance Cost Burden by Firm Type
Horizontal bar chart showing compliance cost as percentage of revenue
for 5 firm types, sorted by burden level.
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
    'title': 'Compliance Cost Burden by Firm Type',
    'type': 'comparison_bar',
    'section': 'Compliance Economics',
    'lecture_number': 4,
}

np.random.seed(42)

# Firm types sorted by compliance cost (ascending for horizontal bars)
firms = ['Large Bank', 'Mid-size Bank', 'Neobank', 'Fintech Startup', 'Crypto Exchange']
costs = [5, 8, 12, 15, 20]  # % of revenue (illustrative)

colors = [V4_COLORS['MLBLUE'], V4_COLORS['MLTEAL'], V4_COLORS['MLORANGE'],
          V4_COLORS['MLPURPLE'], V4_COLORS['MLRED']]

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
fig.patch.set_facecolor('white')

y_pos = np.arange(len(firms))
bars = ax.barh(y_pos, costs, height=0.6, color=colors, edgecolor='white',
               linewidth=1.5, alpha=0.88)

# Value labels
for bar, cost, color in zip(bars, costs, colors):
    ax.text(bar.get_width() + 0.4, bar.get_y() + bar.get_height() / 2,
            f'{cost}%', ha='left', va='center', fontsize=11,
            fontweight='bold', color=color)

ax.set_yticks(y_pos)
ax.set_yticklabels(firms, fontsize=10, fontweight='bold')
ax.set_xlim(0, 25)
ax.xaxis.grid(True, alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

apply_v4_style(ax, title='Compliance Cost as Percentage of Revenue',
               xlabel='Compliance Cost (% of Revenue)')

# Annotation box
ax.text(18, 0.5,
        'Smaller firms bear\ndisproportionate\ncompliance burden',
        ha='center', va='center', fontsize=8.5, color='#888888',
        fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#F5F5F5',
                  edgecolor='#DDDDDD', linewidth=1))

# Threshold line
ax.axvline(x=10, color=V4_COLORS['MLRED'], linewidth=1.5, linestyle='--', alpha=0.5)
ax.text(10.3, 4.3, 'Regulatory\nburden threshold', fontsize=7,
        color=V4_COLORS['MLRED'], fontstyle='italic', alpha=0.7)

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
