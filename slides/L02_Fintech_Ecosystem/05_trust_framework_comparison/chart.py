"""
Figure 05: Trust Framework Comparison
Grouped vertical bars comparing trust dimensions across Banks, Fintech, and BigTech.
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
    'title': 'Trust Framework Comparison',
    'type': 'grouped_bar',
    'section': 'Trust and Adoption',
    'lecture_number': 2,
}

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
fig.patch.set_facecolor('white')

dimensions = ['Institutional\nTrust', 'Technology\nTrust', 'Privacy\nTrust',
              'Brand\nTrust', 'Regulatory\nTrust']
banks = [8, 5, 6, 7, 9]
fintech = [4, 8, 5, 5, 4]
bigtech = [5, 9, 3, 8, 3]

x = np.arange(len(dimensions))
w = 0.25

bars1 = ax.bar(x - w, banks, w, label='Banks', color=V4_COLORS['MLTEAL'],
               edgecolor='white', linewidth=0.5)
bars2 = ax.bar(x, fintech, w, label='Fintech', color=V4_COLORS['MLORANGE'],
               edgecolor='white', linewidth=0.5)
bars3 = ax.bar(x + w, bigtech, w, label='BigTech', color=V4_COLORS['MLPURPLE'],
               edgecolor='white', linewidth=0.5)

# Value labels
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 0.15,
                f'{height}', ha='center', va='bottom', fontsize=8, color='#555555')

ax.set_xticks(x)
ax.set_xticklabels(dimensions, fontsize=9)
ax.set_ylim(0, 11)
ax.set_yticks(range(0, 11, 2))
ax.legend(fontsize=10, frameon=False, loc='upper right')

apply_v4_style(ax, title='Trust Framework: Banks vs Fintech vs BigTech',
               ylabel='Trust Score (1-10)')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
