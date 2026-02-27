"""
Figure 02: Banking Value Chain Disruption
Top: one large box 'Traditional Bank' spanning 5 functions.
Bottom: 5 smaller fintech disruptor boxes with downward arrows.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '_shared'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

try:
    from chart_styles import V4_COLORS, save_chart
except ImportError:
    V4_COLORS = {
        'MLPURPLE': '#9467BD', 'MLBLUE': '#1F77B4', 'MLRED': '#D62728',
        'MLORANGE': '#FF7F0E', 'MLGREEN': '#2CA02C', 'MLGRAY': '#7F7F7F',
        'MLTEAL': '#0D7377', 'MLCYAN': '#14BDEB', 'MLYELLOW': '#BCBD22',
        'MLPINK': '#E377C2', 'MLBROWN': '#8C564B',
    }
    def save_chart(fig, filename='chart.pdf', dpi=300):
        fig.tight_layout()
        fig.savefig(filename, format='pdf', bbox_inches='tight', dpi=dpi, facecolor='white')
        plt.close(fig)
        print(f'Saved: {filename}')

CHART_METADATA = {
    'title': 'Banking Value Chain Disruption',
    'type': 'flowchart',
    'section': 'WHAT',
    'lecture_number': 1,
}

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Title
ax.text(5, 5.7, 'Traditional Banking Value Chain vs. Fintech Unbundling',
        fontsize=13, fontweight='bold', ha='center', va='center', color='#333333')

# --- Top row: Traditional Bank (one large purple box) ---
bank_box = FancyBboxPatch((0.3, 3.8), 9.4, 1.2,
                           boxstyle='round,pad=0.1',
                           facecolor=V4_COLORS['MLPURPLE'], edgecolor='white',
                           linewidth=1.5, alpha=0.90, zorder=3)
ax.add_patch(bank_box)
ax.text(5.0, 4.55, 'TRADITIONAL BANK', fontsize=13, fontweight='bold',
        ha='center', va='center', color='white', zorder=4)
ax.text(5.0, 4.10, 'Vertically integrated: Origination \u2022 Distribution \u2022 Servicing \u2022 Risk Management \u2022 Infrastructure',
        fontsize=8.5, ha='center', va='center', color='#EEE8F5', zorder=4)

# Label above top box
ax.text(0.3, 5.15, 'Traditional Model', fontsize=9, color=V4_COLORS['MLPURPLE'],
        fontweight='bold', va='center')

# --- Bottom row label ---
ax.text(0.3, 3.35, 'Fintech Unbundling', fontsize=9, color=V4_COLORS['MLTEAL'],
        fontweight='bold', va='center')

# Five fintech disruptor boxes
segments = [
    ('Origination', 'Lending\nPlatforms', V4_COLORS['MLTEAL']),
    ('Distribution', 'Neobanks', V4_COLORS['MLBLUE']),
    ('Servicing', 'Robo-\nAdvisors', V4_COLORS['MLORANGE']),
    ('Risk Mgmt', 'RegTech', V4_COLORS['MLRED']),
    ('Infrastructure', 'BaaS\nProviders', V4_COLORS['MLGREEN']),
]

box_width = 1.72
box_gap = 0.145
box_start_x = 0.3

for i, (layer, disruptor, color) in enumerate(segments):
    x0 = box_start_x + i * (box_width + box_gap)
    # Downward arrow from traditional bank
    ax.annotate('', xy=(x0 + box_width / 2, 2.85), xytext=(x0 + box_width / 2, 3.8),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.8))
    # Disruptor box
    fin_box = FancyBboxPatch((x0, 1.8), box_width, 1.0,
                              boxstyle='round,pad=0.08',
                              facecolor=color, edgecolor='white',
                              linewidth=1.2, alpha=0.88, zorder=3)
    ax.add_patch(fin_box)
    ax.text(x0 + box_width / 2, 2.42, disruptor, fontsize=8.5, fontweight='bold',
            ha='center', va='center', color='white', zorder=4)
    # Layer label below box
    ax.text(x0 + box_width / 2, 1.62, layer, fontsize=7.5,
            ha='center', va='center', color='#555555')

# Bottom caption
ax.text(5.0, 0.85, '"Fintech does not replace the bank \u2014 it unbundles it."',
        fontsize=9, ha='center', va='center', color='#555555', style='italic')
ax.text(5.0, 0.42, 'Each startup attacks the most profitable or inefficient piece of the value chain.',
        fontsize=8, ha='center', va='center', color='#888888')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
