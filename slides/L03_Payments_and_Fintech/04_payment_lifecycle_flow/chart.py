"""
Figure 04: Payment Lifecycle Flow
Flowchart of Authorization -> Clearing -> Settlement lifecycle
with timing annotations (seconds, hours, days).
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
    'title': 'Payment Lifecycle Flow',
    'type': 'flowchart',
    'section': 'Payment Infrastructure',
    'lecture_number': 3,
}

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')
fig.patch.set_facecolor('white')

# --- Three main phases as large boxes ---
phases = [
    ('Authorization', 1.8, 4.5, V4_COLORS['MLBLUE']),
    ('Clearing',      5.0, 4.5, V4_COLORS['MLTEAL']),
    ('Settlement',    8.2, 4.5, V4_COLORS['MLPURPLE']),
]

bw, bh = 2.2, 1.2
for label, cx, cy, color in phases:
    box = FancyBboxPatch((cx - bw / 2, cy - bh / 2), bw, bh,
                          boxstyle="round,pad=0.12",
                          facecolor=color, edgecolor='white', linewidth=2, alpha=0.92)
    ax.add_patch(box)
    ax.text(cx, cy, label, ha='center', va='center',
            fontsize=13, fontweight='bold', color='white')

# Arrows between phases
arrow_kw = dict(arrowstyle='->', color='#888888', lw=2.5)
ax.annotate('', xy=(3.8, 4.5), xytext=(2.95, 4.5), arrowprops=arrow_kw)
ax.annotate('', xy=(7.0, 4.5), xytext=(6.15, 4.5), arrowprops=arrow_kw)

# --- Timing annotations ---
timing = [
    (1.8, 3.3, '1-3 seconds', V4_COLORS['MLBLUE']),
    (5.0, 3.3, 'Hours to\nEnd of Day', V4_COLORS['MLTEAL']),
    (8.2, 3.3, '1-3 Business\nDays', V4_COLORS['MLPURPLE']),
]
for cx, cy, label, color in timing:
    bbox_props = dict(boxstyle='round,pad=0.25', facecolor=color, alpha=0.12,
                      edgecolor=color, linewidth=1.2)
    ax.text(cx, cy, label, ha='center', va='center',
            fontsize=9, color=color, fontweight='bold', bbox=bbox_props)

# --- Sub-steps under each phase ---
sub_steps = [
    # Authorization
    [(1.8, 2.0, 'Card data\ntransmitted'), (1.8, 1.2, 'Issuer verifies\nfunds & fraud')],
    # Clearing
    [(5.0, 2.0, 'Transaction data\nbatched'), (5.0, 1.2, 'Network routes\nto issuer')],
    # Settlement
    [(8.2, 2.0, 'Net positions\ncalculated'), (8.2, 1.2, 'Funds transferred\nto merchant')],
]

sub_colors = [V4_COLORS['MLBLUE'], V4_COLORS['MLTEAL'], V4_COLORS['MLPURPLE']]

for phase_idx, steps in enumerate(sub_steps):
    color = sub_colors[phase_idx]
    for i, (sx, sy, slabel) in enumerate(steps):
        box = FancyBboxPatch((sx - 0.85, sy - 0.3), 1.7, 0.6,
                              boxstyle="round,pad=0.06",
                              facecolor='white', edgecolor=color, linewidth=1.5)
        ax.add_patch(box)
        ax.text(sx, sy, slabel, ha='center', va='center',
                fontsize=7.5, color='#444444')
    # Vertical arrows connecting sub-steps
    ax.annotate('', xy=(steps[0][0], steps[0][1] - 0.35),
                xytext=(steps[0][0], steps[0][1] + 0.35),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.2))

# --- Outcome boxes ---
outcomes = [
    (1.8, 0.4, 'Approved /\nDeclined', V4_COLORS['MLGREEN']),
    (5.0, 0.4, 'Records\nMatched', V4_COLORS['MLYELLOW']),
    (8.2, 0.4, 'Merchant\nPaid', V4_COLORS['MLGREEN']),
]
for cx, cy, label, color in outcomes:
    box = FancyBboxPatch((cx - 0.7, cy - 0.25), 1.4, 0.5,
                          boxstyle="round,pad=0.06",
                          facecolor=color, edgecolor='white', linewidth=1.5, alpha=0.85)
    ax.add_patch(box)
    ax.text(cx, cy, label, ha='center', va='center',
            fontsize=8, fontweight='bold', color='white')

# Vertical connectors from sub-steps to outcomes
for phase_idx, steps in enumerate(sub_steps):
    color = sub_colors[phase_idx]
    last_step = steps[-1]
    ax.annotate('', xy=(last_step[0], 0.7),
                xytext=(last_step[0], last_step[1] - 0.35),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.2))

ax.set_title('Payment Transaction Lifecycle',
             fontsize=14, fontweight='bold', pad=15, color='#333333')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
