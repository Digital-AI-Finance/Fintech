"""
Figure 12: Closing Cartoon
XKCD-style cartoon: Two ATMs talking to each other.
One says "Remember when we were the future?"
Caption: "The payment evolution waits for no one."
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
    'title': 'Closing Cartoon: ATM Nostalgia',
    'type': 'cartoon',
    'section': 'Closing',
    'lecture_number': 3,
}

with plt.xkcd():
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.5)
    ax.axis('off')
    fig.patch.set_facecolor('white')

    # Ground line
    ax.plot([0, 12], [0.6, 0.6], color='#888888', linewidth=1.5)

    # === ATM 1 (left) ===
    atm1_x, atm1_y = 3.0, 0.6

    # Body
    atm1_body = Rectangle((atm1_x - 0.8, atm1_y), 1.6, 2.8,
                           facecolor='#B0BEC5', edgecolor='#546E7A', linewidth=2.5)
    ax.add_patch(atm1_body)

    # Screen
    atm1_screen = FancyBboxPatch((atm1_x - 0.55, atm1_y + 1.6), 1.1, 0.8,
                                  boxstyle="round,pad=0.03",
                                  facecolor='#1A237E', edgecolor='#333333', linewidth=1.5)
    ax.add_patch(atm1_screen)
    ax.text(atm1_x, atm1_y + 2.0, 'OUT OF\nSERVICE', ha='center', va='center',
            fontsize=7, fontweight='bold', color=V4_COLORS['MLRED'])

    # Card slot
    ax.add_patch(Rectangle((atm1_x - 0.3, atm1_y + 1.3), 0.6, 0.12,
                            facecolor='#37474F', edgecolor='#263238', linewidth=1))

    # Keypad (small dots)
    for row in range(3):
        for col in range(3):
            ax.plot(atm1_x - 0.2 + col * 0.2, atm1_y + 0.7 + row * 0.15,
                    's', color='#455A64', markersize=4)

    # Cash dispenser slot
    ax.add_patch(Rectangle((atm1_x - 0.4, atm1_y + 0.2), 0.8, 0.15,
                            facecolor='#263238', edgecolor='#1B1B1B', linewidth=1))

    # ATM1 label
    ax.text(atm1_x, atm1_y + 2.65, 'ATM', ha='center', va='center',
            fontsize=8, fontweight='bold', color='#37474F')

    # Cobweb on ATM1
    ax.plot([atm1_x + 0.8, atm1_x + 1.1], [atm1_y + 2.8, atm1_y + 3.1],
            color='#BBBBBB', linewidth=0.8, alpha=0.6)
    ax.plot([atm1_x + 0.8, atm1_x + 1.2], [atm1_y + 2.6, atm1_y + 2.9],
            color='#BBBBBB', linewidth=0.8, alpha=0.6)
    ax.plot([atm1_x + 0.95, atm1_x + 1.15], [atm1_y + 3.1, atm1_y + 2.85],
            color='#BBBBBB', linewidth=0.8, alpha=0.6)

    # "Eyes" on ATM1 screen (anthropomorphized)
    ax.plot(atm1_x - 0.15, atm1_y + 2.15, 'o', color='white', markersize=5)
    ax.plot(atm1_x + 0.15, atm1_y + 2.15, 'o', color='white', markersize=5)
    ax.plot(atm1_x - 0.15, atm1_y + 2.15, 'o', color='#333333', markersize=2)
    ax.plot(atm1_x + 0.15, atm1_y + 2.15, 'o', color='#333333', markersize=2)

    # === ATM 2 (right) ===
    atm2_x, atm2_y = 9.0, 0.6

    # Body
    atm2_body = Rectangle((atm2_x - 0.8, atm2_y), 1.6, 2.8,
                           facecolor='#B0BEC5', edgecolor='#546E7A', linewidth=2.5)
    ax.add_patch(atm2_body)

    # Screen
    atm2_screen = FancyBboxPatch((atm2_x - 0.55, atm2_y + 1.6), 1.1, 0.8,
                                  boxstyle="round,pad=0.03",
                                  facecolor='#1A237E', edgecolor='#333333', linewidth=1.5)
    ax.add_patch(atm2_screen)
    ax.text(atm2_x, atm2_y + 2.0, 'INSERT\nCARD', ha='center', va='center',
            fontsize=7, fontweight='bold', color=V4_COLORS['MLTEAL'])

    # Card slot
    ax.add_patch(Rectangle((atm2_x - 0.3, atm2_y + 1.3), 0.6, 0.12,
                            facecolor='#37474F', edgecolor='#263238', linewidth=1))

    # Keypad
    for row in range(3):
        for col in range(3):
            ax.plot(atm2_x - 0.2 + col * 0.2, atm2_y + 0.7 + row * 0.15,
                    's', color='#455A64', markersize=4)

    # Cash dispenser slot
    ax.add_patch(Rectangle((atm2_x - 0.4, atm2_y + 0.2), 0.8, 0.15,
                            facecolor='#263238', edgecolor='#1B1B1B', linewidth=1))

    # ATM2 label
    ax.text(atm2_x, atm2_y + 2.65, 'ATM', ha='center', va='center',
            fontsize=8, fontweight='bold', color='#37474F')

    # "Eyes" on ATM2 screen
    ax.plot(atm2_x - 0.15, atm2_y + 2.15, 'o', color='white', markersize=5)
    ax.plot(atm2_x + 0.15, atm2_y + 2.15, 'o', color='white', markersize=5)
    ax.plot(atm2_x - 0.15, atm2_y + 2.15, 'o', color='#333333', markersize=2)
    ax.plot(atm2_x + 0.15, atm2_y + 2.15, 'o', color='#333333', markersize=2)

    # Sad mouth on ATM2
    sad = mpatches.Arc((atm2_x, atm2_y + 1.85), 0.25, 0.15, angle=0,
                        theta1=20, theta2=160, color='white', linewidth=1.5)
    ax.add_patch(sad)

    # === Speech bubbles ===
    # ATM1 speech bubble
    bubble1 = FancyBboxPatch((0.3, 4.2), 4.5, 1.2,
                              boxstyle="round,pad=0.2",
                              facecolor='white', edgecolor='#333333', linewidth=1.5)
    ax.add_patch(bubble1)
    ax.text(2.55, 4.8, '"Remember when WE\n  were the future?"',
            ha='center', va='center', fontsize=10.5, fontstyle='italic',
            color='#333333')
    # Bubble tail
    ax.plot([2.8, 3.0, 3.2], [4.2, 3.7, 4.2], color='#333333', linewidth=1.5)

    # ATM2 speech bubble
    bubble2 = FancyBboxPatch((7.2, 4.2), 4.5, 1.2,
                              boxstyle="round,pad=0.2",
                              facecolor='white', edgecolor='#333333', linewidth=1.5)
    ax.add_patch(bubble2)
    ax.text(9.45, 4.8, '"At least the pigeons\n  still visit me."',
            ha='center', va='center', fontsize=10.5, fontstyle='italic',
            color='#333333')
    # Bubble tail
    ax.plot([9.0, 9.1, 9.3], [4.2, 3.7, 4.2], color='#333333', linewidth=1.5)

    # Person walking past in background, looking at phone
    px, py = 6.0, 0.6
    # Legs (walking)
    ax.plot([px, px - 0.2], [py, py + 0.5], color='#AAAAAA', linewidth=1.8)
    ax.plot([px, px + 0.25], [py, py + 0.5], color='#AAAAAA', linewidth=1.8)
    # Torso
    ax.plot([px, px], [py + 0.5, py + 1.1], color='#AAAAAA', linewidth=1.8)
    # Arms
    ax.plot([px, px + 0.4], [py + 0.9, py + 1.0], color='#AAAAAA', linewidth=1.8)
    # Head
    ax.add_patch(plt.Circle((px, py + 1.3), 0.15,
                             facecolor='#DDDDDD', edgecolor='#AAAAAA', linewidth=1.5))
    # Tiny phone
    ax.add_patch(Rectangle((px + 0.3, py + 0.9), 0.18, 0.25,
                            facecolor='#666666', edgecolor='#444444', linewidth=0.8))

    # Caption at bottom
    ax.text(6.0, 0.15, 'The payment evolution waits for no one.',
            ha='center', va='center', fontsize=11, fontstyle='italic',
            color='#555555', fontweight='bold')

    ax.set_title('ATM Nostalgia',
                 fontsize=14, fontweight='bold', pad=15, color='#333333')

output_path = os.path.join(os.path.dirname(__file__), 'cartoon.pdf')
save_chart(fig, output_path)
