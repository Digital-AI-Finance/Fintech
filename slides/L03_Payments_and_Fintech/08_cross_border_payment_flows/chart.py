"""
Figure 08: Cross-Border Payment Flows
Flowchart showing correspondent banking chain: Originator -> Sending Bank ->
Correspondent 1 -> Correspondent 2 -> Receiving Bank -> Beneficiary
with fees at each hop.
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
    'title': 'Cross-Border Payment Flows',
    'type': 'flowchart',
    'section': 'Cross-Border Payments',
    'lecture_number': 3,
}

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.set_xlim(-0.5, 10.5)
ax.set_ylim(0, 7)
ax.axis('off')
fig.patch.set_facecolor('white')

# Chain entities (left to right)
chain = [
    ('Originator',       0.8,  4.0, V4_COLORS['MLBLUE']),
    ('Sending\nBank',    2.8,  4.0, V4_COLORS['MLTEAL']),
    ('Correspondent\nBank 1', 5.0, 4.0, V4_COLORS['MLPURPLE']),
    ('Correspondent\nBank 2', 7.2, 4.0, V4_COLORS['MLPURPLE']),
    ('Receiving\nBank',  9.2,  4.0, V4_COLORS['MLTEAL']),
]

bw, bh = 1.6, 1.0
for label, cx, cy, color in chain:
    box = FancyBboxPatch((cx - bw / 2, cy - bh / 2), bw, bh,
                          boxstyle="round,pad=0.1",
                          facecolor=color, edgecolor='white', linewidth=2, alpha=0.92)
    ax.add_patch(box)
    ax.text(cx, cy, label, ha='center', va='center',
            fontsize=8.5, fontweight='bold', color='white')

# Beneficiary at the end (below Receiving Bank)
ben_box = FancyBboxPatch((9.2 - bw / 2, 1.8 - bh / 2), bw, bh,
                          boxstyle="round,pad=0.1",
                          facecolor=V4_COLORS['MLBLUE'], edgecolor='white',
                          linewidth=2, alpha=0.92)
ax.add_patch(ben_box)
ax.text(9.2, 1.8, 'Beneficiary', ha='center', va='center',
        fontsize=8.5, fontweight='bold', color='white')

# Arrows between chain entities
arrow_kw = dict(arrowstyle='->', color='#777777', lw=2.2)
hop_positions = [
    (0.8 + bw / 2, 4.0, 2.8 - bw / 2, 4.0),
    (2.8 + bw / 2, 4.0, 5.0 - bw / 2, 4.0),
    (5.0 + bw / 2, 4.0, 7.2 - bw / 2, 4.0),
    (7.2 + bw / 2, 4.0, 9.2 - bw / 2, 4.0),
]

fees = ['$15 fee', '$25 fee', '$20 fee', '$10 fee']
fee_colors = [V4_COLORS['MLRED']] * 4

for i, ((x1, y1, x2, y2), fee) in enumerate(zip(hop_positions, fees)):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1), arrowprops=arrow_kw)
    # Fee label above arrow
    mid_x = (x1 + x2) / 2
    ax.text(mid_x, 4.65, fee, ha='center', va='center',
            fontsize=7.5, fontweight='bold', color=V4_COLORS['MLRED'],
            bbox=dict(boxstyle='round,pad=0.15', facecolor=V4_COLORS['MLRED'],
                      alpha=0.1, edgecolor=V4_COLORS['MLRED'], linewidth=0.8))

# Arrow from Receiving Bank down to Beneficiary
ax.annotate('', xy=(9.2, 2.35), xytext=(9.2, 3.45),
            arrowprops=dict(arrowstyle='->', color='#777777', lw=2.2))

# Time annotation
time_box = FancyBboxPatch((2.0, 5.5), 6.0, 0.7,
                           boxstyle="round,pad=0.12",
                           facecolor=V4_COLORS['MLORANGE'], edgecolor='white',
                           linewidth=1.5, alpha=0.15)
ax.add_patch(time_box)
ax.text(5.0, 5.85, 'Typical Duration: 2-5 Business Days    |    Total Fees: ~$70 on $1,000',
        ha='center', va='center', fontsize=8.5, fontweight='bold',
        color=V4_COLORS['MLORANGE'])

# Amount tracking
amounts = ['$1,000', '$985', '$960', '$940', '$930']
positions_x = [0.8, 2.8, 5.0, 7.2, 9.2]
for x, amt in zip(positions_x, amounts):
    ax.text(x, 3.3, amt, ha='center', va='center',
            fontsize=7.5, color='#555555', fontstyle='italic',
            bbox=dict(boxstyle='round,pad=0.15', facecolor='#F0F0F0',
                      edgecolor='#CCCCCC', linewidth=0.8))

# FX conversion note
ax.text(5.0, 2.8, 'FX Conversion', ha='center', va='center',
        fontsize=7, color=V4_COLORS['MLPURPLE'], fontstyle='italic')

# Bottom note
ax.text(5.0, 0.7,
        'Each intermediary adds fees and delays. Fintech solutions aim to reduce both.',
        ha='center', va='center', fontsize=8, color='#777777', fontstyle='italic')

ax.set_title('Cross-Border Payment: Correspondent Banking Chain',
             fontsize=14, fontweight='bold', pad=15, color='#333333')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
