"""
Figure 05: Merchant Cost Comparison
Horizontal bar chart showing cost per $100 transaction by payment type.
ILLUSTRATIVE data only.
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
    'title': 'Merchant Cost per $100 Transaction',
    'type': 'comparison_bar',
    'section': 'Payment Economics',
    'lecture_number': 3,
}

np.random.seed(42)

# ILLUSTRATIVE costs per $100 transaction
payment_types = ['Crypto', 'Debit Card', 'Cash Handling', 'Mobile Wallet', 'Credit Card']
costs = [0.30, 0.80, 1.50, 1.80, 2.50]
colors = [V4_COLORS['MLCYAN'], V4_COLORS['MLBLUE'], V4_COLORS['MLORANGE'],
          V4_COLORS['MLTEAL'], V4_COLORS['MLRED']]

fig, ax = plt.subplots(1, 1, figsize=(10, 6))

bars = ax.barh(payment_types, costs, color=colors, edgecolor='white', linewidth=1.2, height=0.6)

# Value labels
for bar, cost in zip(bars, costs):
    ax.text(bar.get_width() + 0.08, bar.get_y() + bar.get_height() / 2,
            f'${cost:.2f}', ha='left', va='center',
            fontsize=10, fontweight='bold', color='#444444')

ax.set_xlim(0, 3.2)

apply_v4_style(ax,
               title='Merchant Cost per $100 Transaction (Illustrative)',
               xlabel='Cost ($)',
               ylabel='')

# Footnote
fig.text(0.5, -0.02,
         'Costs are illustrative and vary by provider, volume, and region.',
         ha='center', fontsize=7, fontstyle='italic', color='#999999')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
