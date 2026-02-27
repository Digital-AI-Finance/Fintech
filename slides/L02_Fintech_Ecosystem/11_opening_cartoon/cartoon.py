"""
Figure 11: Opening Cartoon
XKCD-style cartoon: Farmer with mobile phone, bank with CLOSED sign.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '_shared'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, Arc
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
    'title': 'Opening Cartoon: Mobile Banking Revolution',
    'type': 'cartoon',
    'section': 'Opening',
    'lecture_number': 2,
}

with plt.xkcd():
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.5)
    ax.axis('off')
    fig.patch.set_facecolor('white')

    # Ground line
    ax.plot([0, 12], [0.8, 0.8], color='#888888', linewidth=1.5)

    # === FARMER (left side) ===
    # Body (stick figure)
    fx, fy = 3.0, 0.8
    # Legs
    ax.plot([fx, fx - 0.3], [fy, fy + 0.8], color='#333333', linewidth=2.5)
    ax.plot([fx, fx + 0.3], [fy, fy + 0.8], color='#333333', linewidth=2.5)
    # Torso
    ax.plot([fx, fx], [fy + 0.8, fy + 1.8], color='#333333', linewidth=2.5)
    # Arms
    ax.plot([fx, fx - 0.5], [fy + 1.5, fy + 1.2], color='#333333', linewidth=2.5)
    ax.plot([fx, fx + 0.6], [fy + 1.5, fy + 1.8], color='#333333', linewidth=2.5)
    # Head
    head = plt.Circle((fx, fy + 2.1), 0.25, facecolor='#FFE0B2', edgecolor='#333333', linewidth=2)
    ax.add_patch(head)
    # Hat (farmer hat)
    ax.plot([fx - 0.4, fx + 0.4], [fy + 2.35, fy + 2.35], color='#8C564B', linewidth=3)
    ax.plot([fx - 0.2, fx + 0.2], [fy + 2.35, fy + 2.55], color='#8C564B', linewidth=5)

    # Phone in hand
    phone = FancyBboxPatch((fx + 0.45, fy + 1.65), 0.35, 0.5,
                            boxstyle="round,pad=0.03",
                            facecolor='#333333', edgecolor='white', linewidth=1)
    ax.add_patch(phone)
    # Phone screen
    screen = FancyBboxPatch((fx + 0.49, fy + 1.72), 0.27, 0.32,
                             boxstyle="round,pad=0.01",
                             facecolor=V4_COLORS['MLTEAL'], edgecolor='none')
    ax.add_patch(screen)
    ax.text(fx + 0.625, fy + 1.88, 'Transfer\nComplete', ha='center', va='center',
            fontsize=4.5, color='white', fontweight='bold')

    # Signal bars above phone
    for i, h in enumerate([0.08, 0.13, 0.18]):
        ax.add_patch(Rectangle((fx + 0.85 + i * 0.08, fy + 2.15), 0.05, h,
                                facecolor=V4_COLORS['MLGREEN'], edgecolor='none'))

    # Speech bubble (farmer)
    bubble = FancyBboxPatch((0.2, 4.0), 4.2, 1.2,
                             boxstyle="round,pad=0.2",
                             facecolor='white', edgecolor='#333333', linewidth=1.5)
    ax.add_patch(bubble)
    ax.text(2.3, 4.6, '"Who needs a branch?\n I have three bars of signal."',
            ha='center', va='center', fontsize=10, fontstyle='italic', color='#333333')
    # Bubble tail
    ax.plot([2.8, 3.0, 3.2], [4.0, 3.6, 4.0], color='#333333', linewidth=1.5)

    # === BANK BUILDING (right side) ===
    bx, by = 8.5, 0.8
    # Foundation
    ax.add_patch(Rectangle((bx - 1.3, by), 2.6, 0.2,
                            facecolor='#CCCCCC', edgecolor='#999999', linewidth=1))
    # Main building
    ax.add_patch(Rectangle((bx - 1.1, by + 0.2), 2.2, 2.0,
                            facecolor='#E0E0E0', edgecolor='#999999', linewidth=1.5))
    # Columns
    for cx_off in [-0.8, -0.3, 0.2, 0.7]:
        ax.add_patch(Rectangle((bx + cx_off, by + 0.2), 0.15, 2.0,
                                facecolor='#BDBDBD', edgecolor='#999999', linewidth=0.5))
    # Roof triangle
    ax.fill([bx - 1.3, bx, bx + 1.3], [by + 2.2, by + 3.0, by + 2.2],
            facecolor='#BDBDBD', edgecolor='#999999', linewidth=1.5)
    # BANK text
    ax.text(bx, by + 2.6, 'BANK', ha='center', va='center',
            fontsize=10, fontweight='bold', color='#666666')
    # Door
    ax.add_patch(Rectangle((bx - 0.25, by + 0.2), 0.5, 0.8,
                            facecolor='#8C564B', edgecolor='#666666', linewidth=1))
    # CLOSED sign
    closed = FancyBboxPatch((bx - 0.55, by + 0.6), 1.1, 0.45,
                             boxstyle="round,pad=0.05",
                             facecolor=V4_COLORS['MLRED'], edgecolor='white', linewidth=1.5)
    ax.add_patch(closed)
    ax.text(bx, by + 0.82, 'CLOSED', ha='center', va='center',
            fontsize=9, fontweight='bold', color='white')

    # Bird on bank roof
    birdx, birdy = bx + 0.6, by + 3.05
    # Simple bird shape
    ax.plot([birdx - 0.15, birdx, birdx + 0.15], [birdy + 0.1, birdy, birdy + 0.1],
            color='#333333', linewidth=2)
    ax.plot([birdx, birdx], [birdy, birdy - 0.12], color='#333333', linewidth=1.5)
    # Bird eye
    ax.plot(birdx + 0.05, birdy + 0.02, 'o', color='#333333', markersize=2)

    # Bird speech bubble
    bird_bubble = FancyBboxPatch((7.8, 4.2), 3.8, 1.0,
                                  boxstyle="round,pad=0.15",
                                  facecolor='white', edgecolor='#333333', linewidth=1.5)
    ax.add_patch(bird_bubble)
    ax.text(9.7, 4.7, '"Even I have\n a mobile wallet."',
            ha='center', va='center', fontsize=9, fontstyle='italic', color='#333333')
    # Bubble tail
    ax.plot([9.0, 9.1, 9.3], [4.2, 3.8, 4.2], color='#333333', linewidth=1.5)

    ax.set_title('The Future of Financial Access',
                 fontsize=14, fontweight='bold', pad=15, color='#333333')

output_path = os.path.join(os.path.dirname(__file__), 'cartoon.pdf')
save_chart(fig, output_path)
