"""
Figure 10: Payment Innovation Timeline
Timeline showing payment disruption waves: 1950s credit cards -> 1990s internet
payments -> 2010s mobile wallets -> 2020s embedded/invisible payments.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '_shared'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
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
    'title': 'Payment Innovation Timeline',
    'type': 'time_series',
    'section': 'Payment Innovation',
    'lecture_number': 3,
}

np.random.seed(42)

# Four disruption waves
waves = [
    {
        'era': 'Wave 1',
        'year': '1950s',
        'title': 'Plastic\nRevolution',
        'examples': 'Diners Club, Visa,\nMasterCard, Amex',
        'color': V4_COLORS['MLBLUE'],
        'x': 1.5,
    },
    {
        'era': 'Wave 2',
        'year': '1990s',
        'title': 'Internet\nPayments',
        'examples': 'PayPal, Online\nBanking, E-commerce',
        'color': V4_COLORS['MLTEAL'],
        'x': 4.0,
    },
    {
        'era': 'Wave 3',
        'year': '2010s',
        'title': 'Mobile\nWallets',
        'examples': 'Apple Pay, M-Pesa,\nAlipay, WeChat Pay',
        'color': V4_COLORS['MLORANGE'],
        'x': 6.5,
    },
    {
        'era': 'Wave 4',
        'year': '2020s',
        'title': 'Embedded &\nInvisible',
        'examples': 'BNPL, Super Apps,\nA2A, Open Banking',
        'color': V4_COLORS['MLPURPLE'],
        'x': 9.0,
    },
]

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.set_xlim(0, 10.5)
ax.set_ylim(0, 7)
ax.axis('off')
fig.patch.set_facecolor('white')

# Timeline arrow
ax.annotate('', xy=(10.2, 3.5), xytext=(0.3, 3.5),
            arrowprops=dict(arrowstyle='->', color='#CCCCCC', lw=3))
ax.text(10.3, 3.5, 'Future', ha='left', va='center',
        fontsize=8, color='#AAAAAA', fontstyle='italic')

# Draw each wave
for wave in waves:
    cx = wave['x']
    color = wave['color']

    # Dot on timeline
    ax.plot(cx, 3.5, 'o', color=color, markersize=14, zorder=5)
    ax.plot(cx, 3.5, 'o', color='white', markersize=8, zorder=6)

    # Year label below timeline
    ax.text(cx, 3.0, wave['year'], ha='center', va='center',
            fontsize=10, fontweight='bold', color=color)

    # Wave label above
    era_box = FancyBboxPatch((cx - 0.9, 4.2), 1.8, 1.8,
                              boxstyle="round,pad=0.12",
                              facecolor=color, edgecolor='white',
                              linewidth=2, alpha=0.9)
    ax.add_patch(era_box)
    ax.text(cx, 5.5, wave['era'], ha='center', va='center',
            fontsize=8, color='white', alpha=0.7)
    ax.text(cx, 4.9, wave['title'], ha='center', va='center',
            fontsize=9, fontweight='bold', color='white')

    # Connector line
    ax.plot([cx, cx], [3.65, 4.2], color=color, linewidth=2, alpha=0.6)

    # Examples below timeline
    ax.text(cx, 2.2, wave['examples'], ha='center', va='center',
            fontsize=7, color='#555555', fontstyle='italic',
            bbox=dict(boxstyle='round,pad=0.2', facecolor=color,
                      alpha=0.08, edgecolor=color, linewidth=0.8))

# Disruption impact annotation
ax.annotate('', xy=(9.5, 1.2), xytext=(1.0, 1.2),
            arrowprops=dict(arrowstyle='->', color='#DDDDDD', lw=2))
ax.text(5.25, 0.8, 'Increasing Speed, Decreasing Friction, Growing Inclusion',
        ha='center', va='center', fontsize=8.5, color='#888888',
        fontstyle='italic')

ax.set_title('Four Waves of Payment Innovation',
             fontsize=14, fontweight='bold', pad=15, color='#333333')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
