"""
Figure 11: Opening Cartoon
XKCD-style cartoon: Compliance officer at desk buried under mountain of
paper regulations. Tiny robot on desk says "I can read all of those in 3 seconds."
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '_shared'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle
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
    'title': "The Compliance Department's New Hire",
    'type': 'cartoon',
    'section': 'Opening',
    'lecture_number': 4,
}

with plt.xkcd():
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis('off')
    fig.patch.set_facecolor('white')

    # Ground line
    ax.plot([0, 12], [0.7, 0.7], color='#888888', linewidth=1.5)

    # === DESK ===
    desk = Rectangle((2.5, 0.7), 5.0, 0.6,
                      facecolor='#D2B48C', edgecolor='#8B7355', linewidth=2)
    ax.add_patch(desk)
    # Desk legs
    ax.plot([2.7, 2.7], [0.7, 0.3], color='#8B7355', linewidth=2.5)
    ax.plot([7.3, 7.3], [0.7, 0.3], color='#8B7355', linewidth=2.5)

    # === COMPLIANCE OFFICER (sitting behind desk) ===
    ox, oy = 4.0, 1.3
    # Torso
    ax.plot([ox, ox], [oy, oy + 1.0], color='#333333', linewidth=2.5)
    # Arms - slumped on desk
    ax.plot([ox, ox - 0.6], [oy + 0.7, oy + 0.3], color='#333333', linewidth=2.5)
    ax.plot([ox, ox + 0.6], [oy + 0.7, oy + 0.3], color='#333333', linewidth=2.5)
    # Head (drooping slightly)
    head = plt.Circle((ox, oy + 1.25), 0.25, facecolor='#FFE0B2',
                       edgecolor='#333333', linewidth=2)
    ax.add_patch(head)
    # Tired expression
    ax.plot([ox - 0.1, ox - 0.05], [oy + 1.3, oy + 1.28], color='#333333', linewidth=1.5)
    ax.plot([ox + 0.05, ox + 0.1], [oy + 1.3, oy + 1.28], color='#333333', linewidth=1.5)
    # Frown
    frown = mpatches.Arc((ox, oy + 1.15), 0.2, 0.12, angle=0,
                           theta1=20, theta2=160, color='#333333', linewidth=1.5)
    ax.add_patch(frown)
    # Sweat drop
    ax.plot([ox + 0.3, ox + 0.32], [oy + 1.35, oy + 1.2], color=V4_COLORS['MLBLUE'],
            linewidth=1.5)

    # === MOUNTAIN OF PAPERS (behind officer, on desk) ===
    paper_x = [2.8, 3.3, 3.8, 4.2, 4.6, 5.1, 5.5, 6.0, 6.5, 7.0]
    paper_y_base = 1.3
    paper_heights = [3.2, 3.8, 4.5, 4.0, 4.8, 4.3, 3.9, 4.6, 3.5, 3.0]

    for px, ph in zip(paper_x, paper_heights):
        # Stack of papers
        for layer in range(int(ph * 2)):
            py = paper_y_base + layer * 0.25
            paper = Rectangle((px - 0.18, py), 0.36, 0.2,
                               facecolor='#FAFAFA', edgecolor='#CCCCCC',
                               linewidth=0.8, alpha=0.9)
            ax.add_patch(paper)
            # Text lines on paper
            ax.plot([px - 0.12, px + 0.12], [py + 0.08, py + 0.08],
                    color='#DDDDDD', linewidth=0.5)
            ax.plot([px - 0.12, px + 0.05], [py + 0.14, py + 0.14],
                    color='#DDDDDD', linewidth=0.5)

    # Labels on some stacks
    stack_labels = [
        (3.3, 4.2, 'GDPR', V4_COLORS['MLBLUE']),
        (4.6, 5.0, 'AML', V4_COLORS['MLRED']),
        (5.5, 4.4, 'MiCA', V4_COLORS['MLPURPLE']),
        (6.5, 4.0, 'BSA', V4_COLORS['MLORANGE']),
    ]
    for sx, sy, slabel, scolor in stack_labels:
        ax.text(sx, sy, slabel, ha='center', va='bottom', fontsize=6.5,
                fontweight='bold', color=scolor, rotation=15)

    # === TINY ROBOT on desk ===
    rx, ry = 8.5, 1.3
    # Robot body
    robot_body = FancyBboxPatch((rx - 0.25, ry), 0.5, 0.45,
                                 boxstyle="round,pad=0.05",
                                 facecolor=V4_COLORS['MLTEAL'],
                                 edgecolor='#333333', linewidth=1.5)
    ax.add_patch(robot_body)
    # Robot head
    robot_head = FancyBboxPatch((rx - 0.2, ry + 0.5), 0.4, 0.3,
                                 boxstyle="round,pad=0.05",
                                 facecolor=V4_COLORS['MLTEAL'],
                                 edgecolor='#333333', linewidth=1.5)
    ax.add_patch(robot_head)
    # Eyes (LED dots)
    ax.plot(rx - 0.08, ry + 0.65, 'o', color=V4_COLORS['MLCYAN'], markersize=4)
    ax.plot(rx + 0.08, ry + 0.65, 'o', color=V4_COLORS['MLCYAN'], markersize=4)
    # Antenna
    ax.plot([rx, rx], [ry + 0.8, ry + 1.0], color='#333333', linewidth=1.5)
    ax.plot(rx, ry + 1.05, 'o', color=V4_COLORS['MLCYAN'], markersize=3)
    # Arms
    ax.plot([rx - 0.25, rx - 0.45], [ry + 0.3, ry + 0.5], color='#333333', linewidth=1.5)
    ax.plot([rx + 0.25, rx + 0.45], [ry + 0.3, ry + 0.5], color='#333333', linewidth=1.5)

    # === ROBOT SPEECH BUBBLE ===
    bubble = FancyBboxPatch((8.5, 3.5), 3.2, 1.6,
                             boxstyle="round,pad=0.2",
                             facecolor='white', edgecolor='#333333', linewidth=1.5)
    ax.add_patch(bubble)
    ax.text(10.1, 4.3, '"I can read ALL\n of those in\n  3 seconds."',
            ha='center', va='center', fontsize=10, fontstyle='italic',
            color='#333333')
    # Bubble tail
    ax.plot([9.0, 8.7, 9.2], [3.5, 2.6, 3.5], color='#333333', linewidth=1.5)

    # === OFFICER SPEECH BUBBLE ===
    bubble2 = FancyBboxPatch((0.3, 4.2), 2.8, 1.0,
                              boxstyle="round,pad=0.2",
                              facecolor='white', edgecolor='#333333', linewidth=1.5)
    ax.add_patch(bubble2)
    ax.text(1.7, 4.7, '"You\'re hired."',
            ha='center', va='center', fontsize=10, fontstyle='italic',
            color='#333333')
    # Bubble tail
    ax.plot([2.5, 3.2, 2.8], [4.2, 3.0, 4.2], color='#333333', linewidth=1.5)

    # Caption
    ax.text(6.0, 0.1,
            "The Compliance Department's New Hire",
            ha='center', va='center', fontsize=12, fontweight='bold',
            color='#555555', fontstyle='italic')

    ax.set_title("The Compliance Department's New Hire",
                 fontsize=14, fontweight='bold', pad=15, color='#333333')

output_path = os.path.join(os.path.dirname(__file__), 'cartoon.pdf')
save_chart(fig, output_path)
