"""
Figure 03: Four-Party Payment Model
Flowchart showing: Cardholder -> Issuer -> Network -> Acquirer -> Merchant
with fee flows annotated using matplotlib patches and arrows.
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
    'title': 'Four-Party Payment Model',
    'type': 'flowchart',
    'section': 'Payment Infrastructure',
    'lecture_number': 3,
}

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')
fig.patch.set_facecolor('white')

# Box positions: [x_center, y_center]
positions = {
    'Cardholder':  (1.5, 5.5),
    'Merchant':    (8.5, 5.5),
    'Issuing\nBank': (1.5, 2.0),
    'Acquiring\nBank': (8.5, 2.0),
    'Card\nNetwork': (5.0, 2.0),
}

box_colors = {
    'Cardholder':  V4_COLORS['MLBLUE'],
    'Merchant':    V4_COLORS['MLORANGE'],
    'Issuing\nBank': V4_COLORS['MLTEAL'],
    'Acquiring\nBank': V4_COLORS['MLPURPLE'],
    'Card\nNetwork': V4_COLORS['MLRED'],
}

box_w, box_h = 1.8, 0.9

# Draw boxes
for label, (cx, cy) in positions.items():
    color = box_colors[label]
    box = FancyBboxPatch((cx - box_w / 2, cy - box_h / 2), box_w, box_h,
                          boxstyle="round,pad=0.1",
                          facecolor=color, edgecolor='white', linewidth=2, alpha=0.92)
    ax.add_patch(box)
    ax.text(cx, cy, label, ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')

# --- Arrows with labels ---
arrow_kw = dict(arrowstyle='->', color='#555555', lw=2,
                connectionstyle='arc3,rad=0.0')
arrow_kw_dashed = dict(arrowstyle='->', color=V4_COLORS['MLRED'], lw=1.5,
                       linestyle='dashed', connectionstyle='arc3,rad=0.0')

# Top: Cardholder -> Merchant  (Goods/Services + Payment)
ax.annotate('', xy=(7.6, 5.7), xytext=(2.4, 5.7), arrowprops=arrow_kw)
ax.text(5.0, 5.95, 'Goods & Services', ha='center', va='center',
        fontsize=8, color='#333333', fontstyle='italic')
ax.annotate('', xy=(2.4, 5.3), xytext=(7.6, 5.3), arrowprops=arrow_kw_dashed)
ax.text(5.0, 5.05, 'Payment (card presented)', ha='center', va='center',
        fontsize=7.5, color=V4_COLORS['MLRED'], fontstyle='italic')

# Left: Cardholder <-> Issuing Bank
ax.annotate('', xy=(1.5, 4.95), xytext=(1.5, 2.55), arrowprops=arrow_kw)
ax.text(0.55, 3.75, 'Statement\n& Billing', ha='center', va='center',
        fontsize=7, color='#555555', rotation=0)

# Right: Merchant <-> Acquiring Bank
ax.annotate('', xy=(8.5, 2.55), xytext=(8.5, 4.95), arrowprops=arrow_kw)
ax.text(9.45, 3.75, 'Settlement\nFunds', ha='center', va='center',
        fontsize=7, color='#555555', rotation=0)

# Bottom: Issuing Bank <-> Network <-> Acquiring Bank
ax.annotate('', xy=(3.95, 2.15), xytext=(2.5, 2.15), arrowprops=arrow_kw)
ax.text(3.2, 2.55, 'Interchange\nFee', ha='center', va='center',
        fontsize=7, color=V4_COLORS['MLTEAL'])
ax.annotate('', xy=(7.5, 2.15), xytext=(6.05, 2.15), arrowprops=arrow_kw)
ax.text(6.8, 2.55, 'Assessment\nFee', ha='center', va='center',
        fontsize=7, color=V4_COLORS['MLPURPLE'])

# Bottom reverse arrows (settlement flow)
ax.annotate('', xy=(2.5, 1.85), xytext=(3.95, 1.85), arrowprops=arrow_kw_dashed)
ax.annotate('', xy=(6.05, 1.85), xytext=(7.5, 1.85), arrowprops=arrow_kw_dashed)
ax.text(5.0, 1.3, 'Settlement & Authorization Flow', ha='center', va='center',
        fontsize=7.5, color=V4_COLORS['MLRED'], fontstyle='italic')

ax.set_title('The Four-Party Card Payment Model',
             fontsize=14, fontweight='bold', pad=15, color='#333333')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
