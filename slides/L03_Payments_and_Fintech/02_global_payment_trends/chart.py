"""
Figure 02: Global Payment Trends by Region
Grouped bar chart showing cash vs. card vs. mobile payment share
by region (US, EU, China, India, Africa). ILLUSTRATIVE data only.
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
    'title': 'Global Payment Trends by Region',
    'type': 'comparison_bar',
    'section': 'Payment Landscape',
    'lecture_number': 3,
}

np.random.seed(42)

regions = ['United\nStates', 'European\nUnion', 'China', 'India', 'Sub-Saharan\nAfrica']

# ILLUSTRATIVE data (% share of transaction volume)
cash =   [18, 30, 10, 45, 70]
card =   [52, 45, 15, 20, 10]
mobile = [30, 25, 75, 35, 20]

x = np.arange(len(regions))
width = 0.25

fig, ax = plt.subplots(1, 1, figsize=(10, 6))

bars_cash = ax.bar(x - width, cash, width, label='Cash',
                   color=V4_COLORS['MLORANGE'], edgecolor='white', linewidth=0.8)
bars_card = ax.bar(x, card, width, label='Card',
                   color=V4_COLORS['MLBLUE'], edgecolor='white', linewidth=0.8)
bars_mobile = ax.bar(x + width, mobile, width, label='Mobile',
                     color=V4_COLORS['MLTEAL'], edgecolor='white', linewidth=0.8)

# Value labels on bars
for bars in [bars_cash, bars_card, bars_mobile]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 1.2,
                f'{int(height)}%', ha='center', va='bottom',
                fontsize=8, fontweight='bold', color='#555555')

ax.set_xticks(x)
ax.set_xticklabels(regions, fontsize=9)
ax.set_ylim(0, 95)
ax.legend(loc='upper right', frameon=True, framealpha=0.9, fontsize=9,
          edgecolor='#CCCCCC')

apply_v4_style(ax,
               title='Global Payment Method Share by Region (Illustrative)',
               xlabel='',
               ylabel='Share of Transactions (%)')

# Footnote
fig.text(0.5, -0.02, 'Data are illustrative and for educational purposes only.',
         ha='center', fontsize=7, fontstyle='italic', color='#999999')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
