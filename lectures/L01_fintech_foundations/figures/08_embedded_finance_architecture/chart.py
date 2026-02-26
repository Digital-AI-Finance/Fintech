"""
Figure 08: Embedded Finance Architecture
Three-layer architecture diagram with dashed API connection arrows.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '_shared'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patches as mpatches

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
    'title': 'Embedded Finance Architecture',
    'type': 'diagram',
    'section': 'WHERE',
    'lecture_number': 1,
}

def draw_layer(ax, y_bot, height, color, alpha, main_label, sub_labels):
    """Draw a full-width layer with label and sublabels."""
    box = FancyBboxPatch((0.3, y_bot), 9.4, height,
                          boxstyle='round,pad=0.08', facecolor=color,
                          edgecolor='white', linewidth=1.5, alpha=alpha, zorder=3)
    ax.add_patch(box)
    mid_y = y_bot + height / 2
    ax.text(0.65, mid_y, main_label, ha='left', va='center',
            fontsize=10, fontweight='bold', color='white', zorder=4)
    # Sublabels as small boxes within layer
    n = len(sub_labels)
    sub_w = 2.0
    sub_h = height * 0.55
    spacing = (9.4 - 0.6 - n * sub_w) / (n + 1)
    for i, lbl in enumerate(sub_labels):
        sx = 0.6 + spacing * (i + 1) + sub_w * i + sub_w / 2 + 0.9
        sub_box = FancyBboxPatch((sx - sub_w / 2, mid_y - sub_h / 2), sub_w, sub_h,
                                  boxstyle='round,pad=0.06', facecolor='white',
                                  edgecolor=color, linewidth=1.2, alpha=0.95, zorder=4)
        ax.add_patch(sub_box)
        ax.text(sx, mid_y, lbl, ha='center', va='center',
                fontsize=8, color='#333333', zorder=5)

def draw_dashed_arrow(ax, x, y1, y2, color):
    ax.annotate('', xy=(x, y2), xytext=(x, y1),
                arrowprops=dict(arrowstyle='<->', color=color, lw=1.6,
                                linestyle='dashed',
                                connectionstyle='arc3,rad=0'))
    ax.text(x + 0.12, (y1 + y2) / 2, 'API', ha='left', va='center',
            fontsize=7.5, color=color, fontweight='bold')

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Title
ax.text(5, 5.72, 'Embedded Finance: Financial Services Inside Non-Financial Platforms',
        fontsize=12.5, fontweight='bold', ha='center', va='center', color='#333333')

# Layer 1 (Top): Consumer-facing platforms
draw_layer(ax, 4.2, 1.1, V4_COLORS['MLORANGE'], 0.88,
           'Consumer Platforms',
           ['Ride-Sharing', 'E-Commerce', 'Social Media', 'Super-Apps'])

# Layer 2 (Middle): Embedded financial services
draw_layer(ax, 2.5, 1.1, V4_COLORS['MLPURPLE'], 0.88,
           'Embedded Finance APIs',
           ['Payments', 'Lending', 'Insurance'])

# Layer 3 (Bottom): Licensed infrastructure
draw_layer(ax, 0.8, 1.1, V4_COLORS['MLBLUE'], 0.88,
           'Licensed Infrastructure',
           ['Banks', 'Payment Networks', 'Insurers'])

# Dashed API arrows between layers
draw_dashed_arrow(ax, 1.8, 3.62, 4.18, V4_COLORS['MLPURPLE'])
draw_dashed_arrow(ax, 1.8, 1.92, 2.48, V4_COLORS['MLBLUE'])

# Layer labels on right
ax.text(9.75, 4.75, 'Layer 3\n(Top)', ha='center', va='center',
        fontsize=7.5, color=V4_COLORS['MLORANGE'], fontweight='bold')
ax.text(9.75, 3.05, 'Layer 2\n(Middle)', ha='center', va='center',
        fontsize=7.5, color=V4_COLORS['MLPURPLE'], fontweight='bold')
ax.text(9.75, 1.35, 'Layer 1\n(Bottom)', ha='center', va='center',
        fontsize=7.5, color=V4_COLORS['MLBLUE'], fontweight='bold')

# Caption
ax.text(5.0, 0.38, '"Financial services invisible to the consumer \u2014 integrated into platforms they already use."',
        fontsize=8.5, ha='center', va='center', color='#555555', style='italic')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
