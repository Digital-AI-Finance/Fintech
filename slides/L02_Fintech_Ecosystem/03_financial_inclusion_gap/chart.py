"""
Figure 03: Financial Inclusion Gap
Grouped horizontal bars showing bank account vs mobile money access by region.
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
    'title': 'Financial Inclusion Gap',
    'type': 'grouped_horizontal_bar',
    'section': 'Financial Inclusion',
    'lecture_number': 2,
}

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
fig.patch.set_facecolor('white')

regions = ['Sub-Saharan Africa', 'South Asia', 'East Asia', 'Latin America', 'MENA', 'Developed']
bank = [43, 68, 80, 73, 53, 95]
mobile = [75, 82, 90, 85, 78, 95]

y_pos = np.arange(len(regions))
bar_h = 0.35

bars_mobile = ax.barh(y_pos - bar_h / 2, mobile, bar_h, label='Mobile Money Access',
                       color=V4_COLORS['MLORANGE'], edgecolor='white', linewidth=0.5)
bars_bank = ax.barh(y_pos + bar_h / 2, bank, bar_h, label='Bank Account Access',
                     color=V4_COLORS['MLTEAL'], edgecolor='white', linewidth=0.5)

# Gap shading between bank and mobile
for i in range(len(regions)):
    if mobile[i] > bank[i]:
        gap = mobile[i] - bank[i]
        ax.barh(y_pos[i], gap, 0.8, left=bank[i],
                color=V4_COLORS['MLYELLOW'], alpha=0.15, zorder=0)
        ax.text(bank[i] + gap / 2, y_pos[i], f'+{gap}pp',
                ha='center', va='center', fontsize=7, color='#888888', fontstyle='italic')

# Value labels
for bar_set in [bars_bank, bars_mobile]:
    for bar in bar_set:
        width = bar.get_width()
        ax.text(width + 1, bar.get_y() + bar.get_height() / 2,
                f'{width:.0f}%', ha='left', va='center', fontsize=8, color='#555555')

ax.set_yticks(y_pos)
ax.set_yticklabels(regions, fontsize=10)
ax.set_xlim(0, 105)
ax.legend(fontsize=9, frameon=False, loc='lower right')

apply_v4_style(ax, title='Financial Inclusion Gap: Bank Access vs Mobile Money',
               xlabel='Population with Access (%)')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
