"""
Figure 04: Three Stages of Money Laundering
Three-column flowchart showing Placement, Layering, and Integration stages
with methods and a detection difficulty gradient.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '_shared'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
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
    'title': 'Three Stages of Money Laundering',
    'type': 'flowchart',
    'section': 'AML/KYC Compliance',
    'lecture_number': 4,
}

np.random.seed(42)

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 7.5)
ax.axis('off')
fig.patch.set_facecolor('white')

# Three stage columns
stages = [
    ('PLACEMENT', 1.8, V4_COLORS['MLBLUE'],
     ['Cash deposits', 'Smurfing', 'Shell companies', 'Currency exchange']),
    ('LAYERING', 5.0, V4_COLORS['MLORANGE'],
     ['Complex transfers', 'Cross-border wires', 'Shell networks', 'Crypto mixing']),
    ('INTEGRATION', 8.2, V4_COLORS['MLRED'],
     ['Real estate', 'Legitimate business', 'Luxury goods', 'Investments']),
]

# Stage headers
for label, cx, color, methods in stages:
    # Header box
    header = FancyBboxPatch((cx - 1.3, 6.2), 2.6, 0.8,
                             boxstyle="round,pad=0.12",
                             facecolor=color, edgecolor='white', linewidth=2, alpha=0.95)
    ax.add_patch(header)
    ax.text(cx, 6.6, label, ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')

    # Method boxes
    for j, method in enumerate(methods):
        y = 5.2 - j * 0.9
        mbox = FancyBboxPatch((cx - 1.15, y - 0.3), 2.3, 0.6,
                               boxstyle="round,pad=0.08",
                               facecolor=color, edgecolor=color,
                               linewidth=1.2, alpha=0.15)
        ax.add_patch(mbox)
        ax.text(cx, y, method, ha='center', va='center',
                fontsize=8.5, color=color, fontweight='bold')

# Arrows between stages
arrow_kw = dict(arrowstyle='->', color='#555555', lw=2.5)
ax.annotate('', xy=(3.5, 6.6), xytext=(3.1, 6.6), arrowprops=arrow_kw)
ax.annotate('', xy=(6.7, 6.6), xytext=(6.3, 6.6), arrowprops=arrow_kw)

# Difficulty gradient bar at bottom
gradient_y = 0.6
bar_height = 0.35
for i in range(100):
    x = 1.0 + i * 0.08
    ratio = i / 99.0
    r = int(31 + ratio * (214 - 31))
    g = int(119 + ratio * (39 - 119))
    b = int(180 + ratio * (40 - 180))
    color_hex = f'#{r:02x}{g:02x}{b:02x}'
    ax.fill_between([x, x + 0.08], gradient_y - bar_height / 2,
                    gradient_y + bar_height / 2, color=color_hex)

ax.text(1.0, gradient_y, 'Easier', ha='right', va='center',
        fontsize=8, color=V4_COLORS['MLBLUE'], fontweight='bold')
ax.text(9.0, gradient_y, 'Harder', ha='left', va='center',
        fontsize=8, color=V4_COLORS['MLRED'], fontweight='bold')
ax.text(5.0, gradient_y - 0.45, 'Detection Difficulty',
        ha='center', va='center', fontsize=8, color='#888888', fontstyle='italic')

ax.set_title('Three Stages of Money Laundering',
             fontsize=14, fontweight='bold', pad=15, color='#333333')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
