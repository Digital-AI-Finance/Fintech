"""
Figure 07: Bank-Fintech Partnership Flow
Three-layer flow: Bank -> Joint Product <- Fintech -> Consumer.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '_shared'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

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
    'title': 'Bank-Fintech Partnership Flow',
    'type': 'flowchart',
    'section': 'HOW',
    'lecture_number': 1,
}

def draw_box(ax, x, y, w, h, color, title, items=None, fontsize=9, alpha=0.90):
    box = FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                          boxstyle='round,pad=0.1', facecolor=color,
                          edgecolor='white', linewidth=1.5, alpha=alpha, zorder=3)
    ax.add_patch(box)
    ax.text(x, y + h / 2 - 0.22, title, ha='center', va='top',
            fontsize=fontsize + 0.5, color='white', fontweight='bold', zorder=4)
    if items:
        for i, item in enumerate(items):
            ax.text(x, y + h / 2 - 0.52 - i * 0.28, item,
                    ha='center', va='top', fontsize=fontsize - 1,
                    color='white', zorder=4)

def draw_arrow(ax, x1, y1, x2, y2, color, label='', lw=2.0):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                connectionstyle='arc3,rad=0'))
    if label:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        ax.text(mx, my + 0.1, label, ha='center', va='bottom',
                fontsize=7.5, color=color, fontweight='bold')

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Title
ax.text(5, 5.72, 'How a Bank\u2013Fintech Partnership Works',
        fontsize=13, fontweight='bold', ha='center', va='center', color='#333333')

# --- Top row: Bank (left) + Joint Product (center) + Fintech (right) ---
top_y = 3.9
bw, bh = 2.4, 1.8

# Bank box
draw_box(ax, 1.5, top_y, bw, bh, V4_COLORS['MLPURPLE'], 'BANK',
         items=['\u2022 Banking License', '\u2022 Customer Base', '\u2022 Capital', '\u2022 Compliance'],
         fontsize=8.5)

# Fintech box
draw_box(ax, 8.5, top_y, bw, bh, V4_COLORS['MLORANGE'], 'FINTECH',
         items=['\u2022 Technology Platform', '\u2022 UX Design', '\u2022 Speed', '\u2022 Innovation'],
         fontsize=8.5)

# Joint Product (center)
draw_box(ax, 5.0, top_y, 2.2, bh, V4_COLORS['MLGREEN'], 'JOINT\nPRODUCT',
         items=['Combined offering', 'to market'], fontsize=8.5)

# Arrows from bank and fintech toward center
draw_arrow(ax, 2.72, top_y, 3.9, top_y, V4_COLORS['MLPURPLE'], 'provides')
draw_arrow(ax, 7.28, top_y, 6.1, top_y, V4_COLORS['MLORANGE'], 'provides')

# Downward arrow from Joint Product to Consumer
draw_arrow(ax, 5.0, top_y - bh / 2, 5.0, 1.82, V4_COLORS['MLGREEN'], 'delivered to')

# Consumer box at bottom
draw_box(ax, 5.0, 1.35, 3.4, 0.80, V4_COLORS['MLBLUE'], 'CONSUMER',
         items=['Improved financial experience'], fontsize=8.5)

# Left labels
ax.text(1.5, 1.9, 'What the Bank brings:', fontsize=7.5, ha='center', color=V4_COLORS['MLPURPLE'],
        fontweight='bold')
ax.text(8.5, 1.9, 'What the Fintech brings:', fontsize=7.5, ha='center', color=V4_COLORS['MLORANGE'],
        fontweight='bold')

# Bottom caption
ax.text(5.0, 0.38, '"A partnership succeeds when each party contributes something the other cannot build faster alone."',
        fontsize=8, ha='center', va='center', color='#555555', style='italic')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
