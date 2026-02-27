"""
Figure 12: Closing Cartoon
XKCD-style cartoon: Designer at whiteboard with nudge ethics columns.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '_shared'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
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
    def save_chart(fig, filename='cartoon.pdf', dpi=300):
        fig.tight_layout()
        fig.savefig(filename, format='pdf', bbox_inches='tight', dpi=dpi, facecolor='white')
        plt.close(fig)
        print(f'Saved: {filename}')

CHART_METADATA = {
    'title': 'Closing Cartoon: Ethical Choice Architecture',
    'type': 'cartoon',
    'section': 'Closing',
    'lecture_number': 2,
}

with plt.xkcd():
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.5)
    ax.axis('off')
    fig.patch.set_facecolor('white')

    # Ground line
    ax.plot([0, 12], [0.5, 0.5], color='#CCCCCC', linewidth=1)

    # === WHITEBOARD ===
    wb_x, wb_y = 3.5, 1.5
    wb_w, wb_h = 5.0, 3.8
    # Board frame
    ax.add_patch(Rectangle((wb_x, wb_y), wb_w, wb_h,
                            facecolor='white', edgecolor='#666666', linewidth=2.5))
    # Board legs
    ax.plot([wb_x + 0.5, wb_x + 0.5], [wb_y, 0.5], color='#666666', linewidth=2)
    ax.plot([wb_x + wb_w - 0.5, wb_x + wb_w - 0.5], [wb_y, 0.5], color='#666666', linewidth=2)
    # Tray
    ax.add_patch(Rectangle((wb_x, wb_y - 0.08), wb_w, 0.08,
                            facecolor='#999999', edgecolor='none'))

    # Dividing line on whiteboard
    ax.plot([wb_x + wb_w / 2, wb_x + wb_w / 2], [wb_y + 0.3, wb_y + wb_h - 0.3],
            color='#333333', linewidth=1.5)

    # Left column header: "Nudges that help users"
    ax.text(wb_x + wb_w * 0.25, wb_y + wb_h - 0.5, 'Nudges that\nhelp users',
            ha='center', va='center', fontsize=10, fontweight='bold',
            color=V4_COLORS['MLGREEN'])

    # Left column items
    left_items = ['Auto-save defaults', 'Clear fee display',
                  'Spending alerts', 'Simple opt-out']
    for i, item in enumerate(left_items):
        yy = wb_y + wb_h - 1.2 - i * 0.6
        ax.text(wb_x + 0.3, yy, f'  {item}', fontsize=8, color='#333333', va='center')
        # Checkmark
        ax.text(wb_x + 0.15, yy, '+', fontsize=10, color=V4_COLORS['MLGREEN'],
                fontweight='bold', va='center')

    # Right column header: "Nudges that help us"
    ax.text(wb_x + wb_w * 0.75, wb_y + wb_h - 0.5, 'Nudges that\nhelp us',
            ha='center', va='center', fontsize=10, fontweight='bold',
            color=V4_COLORS['MLRED'])

    # Right column items
    right_items = ['Hidden fees', 'Dark patterns',
                   'Confusing opt-outs', 'Addictive loops']
    for i, item in enumerate(right_items):
        yy = wb_y + wb_h - 1.2 - i * 0.6
        ax.text(wb_x + wb_w / 2 + 0.3, yy, f'  {item}', fontsize=8, color='#333333', va='center')
        # X mark
        ax.text(wb_x + wb_w / 2 + 0.15, yy, 'x', fontsize=10, color=V4_COLORS['MLRED'],
                fontweight='bold', va='center')

    # === DESIGNER (left of whiteboard) ===
    dx, dy = 2.0, 0.5
    # Legs
    ax.plot([dx, dx - 0.2], [dy, dy + 0.7], color='#333333', linewidth=2.5)
    ax.plot([dx, dx + 0.2], [dy, dy + 0.7], color='#333333', linewidth=2.5)
    # Torso
    ax.plot([dx, dx], [dy + 0.7, dy + 1.6], color='#333333', linewidth=2.5)
    # Arms: right arm pointing at board
    ax.plot([dx, dx - 0.4], [dy + 1.3, dy + 1.0], color='#333333', linewidth=2.5)
    ax.plot([dx, dx + 0.8], [dy + 1.3, dy + 1.6], color='#333333', linewidth=2.5)
    # Pointer line
    ax.plot([dx + 0.8, wb_x + 0.3], [dy + 1.6, wb_y + wb_h / 2], color='#666666',
            linewidth=1.5, linestyle='--')
    # Head
    head = plt.Circle((dx, dy + 1.85), 0.22, facecolor='#FFE0B2',
                       edgecolor='#333333', linewidth=2)
    ax.add_patch(head)
    # Glasses
    ax.plot([dx - 0.15, dx + 0.15], [dy + 1.88, dy + 1.88], color='#333333', linewidth=1.5)
    ax.add_patch(plt.Circle((dx - 0.1, dy + 1.88), 0.06, facecolor='none',
                             edgecolor='#333333', linewidth=1.5))
    ax.add_patch(plt.Circle((dx + 0.1, dy + 1.88), 0.06, facecolor='none',
                             edgecolor='#333333', linewidth=1.5))

    # === COLLEAGUE (right of whiteboard) ===
    cx, cy = 10.0, 0.5
    # Legs
    ax.plot([cx, cx - 0.2], [cy, cy + 0.7], color='#333333', linewidth=2.5)
    ax.plot([cx, cx + 0.2], [cy, cy + 0.7], color='#333333', linewidth=2.5)
    # Torso
    ax.plot([cx, cx], [cy + 0.7, cy + 1.6], color='#333333', linewidth=2.5)
    # Arms (folded/thinking)
    ax.plot([cx, cx - 0.5], [cy + 1.3, cy + 1.1], color='#333333', linewidth=2.5)
    ax.plot([cx, cx + 0.3], [cy + 1.3, cy + 1.5], color='#333333', linewidth=2.5)
    # Head
    head2 = plt.Circle((cx, cy + 1.85), 0.22, facecolor='#FFE0B2',
                        edgecolor='#333333', linewidth=2)
    ax.add_patch(head2)

    # Colleague speech bubble
    bubble = FancyBboxPatch((8.8, 3.8), 3.0, 1.5,
                             boxstyle="round,pad=0.2",
                             facecolor='white', edgecolor='#333333', linewidth=1.5)
    ax.add_patch(bubble)
    ax.text(10.3, 4.55, '"Good choice architecture:\nmake the ethical option\nthe easy option."',
            ha='center', va='center', fontsize=8.5, fontstyle='italic', color='#333333')
    # Bubble tail
    ax.plot([10.0, 10.0, 10.2], [3.8, 3.4, 3.8], color='#333333', linewidth=1.5)

    ax.set_title('The Ethics of Nudging in Finance',
                 fontsize=14, fontweight='bold', pad=15, color='#333333')

output_path = os.path.join(os.path.dirname(__file__), 'cartoon.pdf')
save_chart(fig, output_path)
