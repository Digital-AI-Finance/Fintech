"""
Figure 05: US Fintech Regulatory Landscape
Two-tier diagram showing Federal regulators (OCC, SEC, CFTC, CFPB, FinCEN, FDIC)
and State-level regulators with jurisdiction overlaps and connecting lines.
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
    'title': 'US Fintech Regulatory Landscape',
    'type': 'diagram',
    'section': 'Regulatory Landscape',
    'lecture_number': 4,
}

np.random.seed(42)

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')
fig.patch.set_facecolor('white')

# --- Federal Tier ---
fed_label_y = 7.2
ax.text(5.0, fed_label_y, 'FEDERAL REGULATORS', ha='center', va='center',
        fontsize=11, fontweight='bold', color=V4_COLORS['MLBLUE'],
        bbox=dict(boxstyle='round,pad=0.3', facecolor=V4_COLORS['MLBLUE'],
                  alpha=0.1, edgecolor=V4_COLORS['MLBLUE'], linewidth=1.5))

federal = [
    ('OCC', 1.2, 'Banking\nCharters', V4_COLORS['MLBLUE']),
    ('SEC', 2.95, 'Securities\n& Tokens', V4_COLORS['MLTEAL']),
    ('CFTC', 4.7, 'Derivatives\n& Commodities', V4_COLORS['MLPURPLE']),
    ('CFPB', 6.45, 'Consumer\nProtection', V4_COLORS['MLGREEN']),
    ('FinCEN', 8.2, 'AML/BSA\nEnforcement', V4_COLORS['MLORANGE']),
]

# FDIC spans wider -- draw separately
fdic_y = 5.0
fdic_box = FancyBboxPatch((0.5, fdic_y - 0.3), 9.0, 0.6,
                            boxstyle="round,pad=0.1",
                            facecolor=V4_COLORS['MLRED'], edgecolor='white',
                            linewidth=2, alpha=0.15)
ax.add_patch(fdic_box)
ax.text(5.0, fdic_y, 'FDIC  --  Deposit Insurance & Prudential Oversight (cross-cutting)',
        ha='center', va='center', fontsize=8.5, fontweight='bold',
        color=V4_COLORS['MLRED'])

box_w, box_h = 1.4, 0.9
fed_y = 6.1

for name, cx, desc, color in federal:
    box = FancyBboxPatch((cx - box_w / 2, fed_y - box_h / 2), box_w, box_h,
                          boxstyle="round,pad=0.1",
                          facecolor=color, edgecolor='white', linewidth=2, alpha=0.92)
    ax.add_patch(box)
    ax.text(cx, fed_y + 0.1, name, ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')
    ax.text(cx, fed_y - 0.25, desc, ha='center', va='center',
            fontsize=6, color='white', alpha=0.9)

# --- State Tier ---
state_label_y = 3.6
ax.text(5.0, state_label_y, 'STATE-LEVEL REGULATORS', ha='center', va='center',
        fontsize=11, fontweight='bold', color=V4_COLORS['MLBROWN'],
        bbox=dict(boxstyle='round,pad=0.3', facecolor=V4_COLORS['MLBROWN'],
                  alpha=0.1, edgecolor=V4_COLORS['MLBROWN'], linewidth=1.5))

state_items = [
    ('50 State\nRegulators', 2.2, V4_COLORS['MLBROWN']),
    ('Money\nTransmitter\nLicenses', 5.0, V4_COLORS['MLBROWN']),
    ('State\nConsumer\nProtection', 7.8, V4_COLORS['MLBROWN']),
]

state_y = 2.5
for name, cx, color in state_items:
    box = FancyBboxPatch((cx - box_w / 2, state_y - box_h / 2), box_w, box_h,
                          boxstyle="round,pad=0.1",
                          facecolor=color, edgecolor='white', linewidth=2, alpha=0.85)
    ax.add_patch(box)
    ax.text(cx, state_y, name, ha='center', va='center',
            fontsize=8, fontweight='bold', color='white')

# Connecting lines (overlap indicators)
overlap_pairs = [
    (1.2, fed_y, 2.2, state_y),    # OCC -> 50 State
    (2.95, fed_y, 2.2, state_y),   # SEC -> 50 State
    (6.45, fed_y, 7.8, state_y),   # CFPB -> State Consumer
    (8.2, fed_y, 5.0, state_y),    # FinCEN -> MTLs
    (4.7, fed_y, 5.0, state_y),    # CFTC -> MTLs
]

for fx, fy, sx, sy in overlap_pairs:
    ax.plot([fx, sx], [fy - box_h / 2 - 0.05, sy + box_h / 2 + 0.35],
            color='#AAAAAA', linewidth=1.0, linestyle=':', alpha=0.7)

# Overlap annotation
ax.text(5.0, 1.2,
        'Fintech firms may face overlapping jurisdiction from multiple federal\n'
        'AND state regulators simultaneously -- no single unified framework.',
        ha='center', va='center', fontsize=8, color='#888888', fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#F5F5F5',
                  edgecolor='#DDDDDD', linewidth=1))

ax.set_title('US Fintech Regulatory Landscape: The Patchwork Problem',
             fontsize=14, fontweight='bold', pad=15, color='#333333')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
