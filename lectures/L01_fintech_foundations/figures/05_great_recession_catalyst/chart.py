"""
Figure 05: Great Recession as Catalyst
Sequential causal chain flowchart, left-to-right with colored boxes and arrows.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '_shared'))

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
    'title': 'Great Recession Catalyst Chain',
    'type': 'flowchart',
    'section': 'CASE',
    'lecture_number': 1,
}

def draw_box(ax, x, y, w, h, color, text, fontsize=8.5, text_color='white', alpha=0.90):
    box = FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                          boxstyle='round,pad=0.08', facecolor=color,
                          edgecolor='white', linewidth=1.2, alpha=alpha, zorder=3)
    ax.add_patch(box)
    lines = text.split('\n')
    for li, line in enumerate(lines):
        offset = (len(lines) - 1) / 2 * 0.10 - li * 0.10
        ax.text(x, y + offset, line, ha='center', va='center',
                fontsize=fontsize, color=text_color, fontweight='bold', zorder=4)

def draw_arrow(ax, x1, y1, x2, y2, color='#888888'):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.6,
                                connectionstyle='arc3,rad=0.0'))

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Title
ax.text(5, 5.72, 'The 2008 Crisis: A Catalyst for Fintech Innovation',
        fontsize=13, fontweight='bold', ha='center', va='center', color='#333333')

# --- Row 1: Crisis chain (red) ---
crisis_y = 4.3
crisis_boxes = [
    (1.0, 'Housing\nBubble'),
    (2.8, 'Bank\nFailures'),
    (4.6, 'Government\nBailouts'),
    (6.4, 'Consumer\nTrust Erosion'),
    (8.2, 'Regulatory\nResponse'),
]
box_w, box_h = 1.45, 0.72
for x, label in crisis_boxes:
    color = V4_COLORS['MLORANGE'] if 'Regulatory' in label else V4_COLORS['MLRED']
    draw_box(ax, x, crisis_y, box_w, box_h, color, label, fontsize=8)

# Arrows between crisis boxes
for i in range(len(crisis_boxes) - 1):
    x1 = crisis_boxes[i][0] + box_w / 2
    x2 = crisis_boxes[i + 1][0] - box_w / 2
    draw_arrow(ax, x1, crisis_y, x2, crisis_y, color=V4_COLORS['MLRED'])

# Divider label
ax.text(0.2, 3.55, 'leads to\u2192', fontsize=8, color='#888888', va='center', style='italic')
ax.axhline(y=3.5, color='#DDDDDD', linewidth=0.8, xmin=0.08, xmax=0.92)

# --- Row 2: Three parallel outcomes (green) ---
outcome_y = 2.6
outcomes = [
    (2.2, 'Demand for\nAlternatives'),
    (5.0, 'Regulatory\nSpace Opens'),
    (7.8, 'Available\nTalent'),
]
for x, label in outcomes:
    draw_box(ax, x, outcome_y, 2.2, 0.72, V4_COLORS['MLTEAL'], label, fontsize=8.5)
    # Vertical arrow from Regulatory Response box
    draw_arrow(ax, 8.2, crisis_y - box_h / 2, x, outcome_y + box_h / 2,
               color=V4_COLORS['MLORANGE'])

# Arrow from each outcome to Fintech Boom
for x, _ in outcomes:
    draw_arrow(ax, x, outcome_y - box_h / 2, 5.0, 1.62, color=V4_COLORS['MLGREEN'])

# --- Fintech Boom box (bottom center) ---
draw_box(ax, 5.0, 1.2, 3.0, 0.72, V4_COLORS['MLGREEN'],
         'FINTECH BOOM\n2010s \u2192 present', fontsize=9)

# Caption
ax.text(5.0, 0.35, 'Illustrative causal chain \u2014 conceptual model only.',
        fontsize=7.5, ha='center', va='center', color='#888888', style='italic')

# Legend patches
legend_items = [
    mpatches.Patch(color=V4_COLORS['MLRED'], label='Crisis Events'),
    mpatches.Patch(color=V4_COLORS['MLORANGE'], label='Regulatory Response'),
    mpatches.Patch(color=V4_COLORS['MLTEAL'], label='Enabling Conditions'),
    mpatches.Patch(color=V4_COLORS['MLGREEN'], label='Fintech Outcome'),
]
ax.legend(handles=legend_items, loc='lower right', fontsize=7.5, framealpha=0.9,
          ncol=2)

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
