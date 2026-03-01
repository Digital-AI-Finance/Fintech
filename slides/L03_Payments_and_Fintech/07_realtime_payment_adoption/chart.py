"""
Figure 07: Real-Time Payment Adoption
Bar chart showing illustrative real-time payment transaction volumes
for UPI (India), PIX (Brazil), FedNow (US), Faster Payments (UK),
SEPA Instant (EU).
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
    'title': 'Real-Time Payment Adoption Worldwide',
    'type': 'comparison_bar',
    'section': 'Payment Innovation',
    'lecture_number': 3,
}

np.random.seed(42)

# ILLUSTRATIVE annual transaction volumes (billions)
systems = ['UPI\n(India)', 'PIX\n(Brazil)', 'SEPA Instant\n(EU)',
           'Faster Payments\n(UK)', 'FedNow\n(US)']
volumes = [120, 42, 18, 8, 2]
colors = [V4_COLORS['MLORANGE'], V4_COLORS['MLGREEN'], V4_COLORS['MLBLUE'],
          V4_COLORS['MLTEAL'], V4_COLORS['MLPURPLE']]

fig, ax = plt.subplots(1, 1, figsize=(10, 6))

bars = ax.bar(systems, volumes, color=colors, edgecolor='white', linewidth=1.2, width=0.6)

# Value labels
for bar, vol in zip(bars, volumes):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2,
            f'{vol}B', ha='center', va='bottom',
            fontsize=10, fontweight='bold', color='#444444')

ax.set_ylim(0, 145)

apply_v4_style(ax,
               title='Real-Time Payment Systems: Transaction Volumes (Illustrative)',
               xlabel='',
               ylabel='Annual Transactions (Billions)')

# Launch year annotations
launch_years = ['2016', '2020', '2017', '2008', '2023']
for bar, year in zip(bars, launch_years):
    ax.text(bar.get_x() + bar.get_width() / 2, 3,
            f'Est. {year}', ha='center', va='bottom',
            fontsize=7, color='white', fontstyle='italic', fontweight='bold')

fig.text(0.5, -0.02,
         'Volumes are illustrative and for educational purposes only.',
         ha='center', fontsize=7, fontstyle='italic', color='#999999')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
