"""
Figure 11: Opening Cartoon
XKCD-style cartoon: Person paying with phone, cashier confused by physical cash.
Caption: "Sorry, we don't accept... whatever that is."
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
    'title': 'Opening Cartoon: Cash Not Accepted',
    'type': 'cartoon',
    'section': 'Opening',
    'lecture_number': 3,
}

with plt.xkcd():
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.5)
    ax.axis('off')
    fig.patch.set_facecolor('white')

    # Ground line
    ax.plot([0, 12], [0.8, 0.8], color='#888888', linewidth=1.5)

    # === CUSTOMER (left side) - paying with phone ===
    cx, cy = 3.5, 0.8
    # Legs
    ax.plot([cx, cx - 0.3], [cy, cy + 0.8], color='#333333', linewidth=2.5)
    ax.plot([cx, cx + 0.3], [cy, cy + 0.8], color='#333333', linewidth=2.5)
    # Torso
    ax.plot([cx, cx], [cy + 0.8, cy + 1.8], color='#333333', linewidth=2.5)
    # Arms - right arm holding phone forward
    ax.plot([cx, cx - 0.5], [cy + 1.5, cy + 1.2], color='#333333', linewidth=2.5)
    ax.plot([cx, cx + 0.7], [cy + 1.5, cy + 1.6], color='#333333', linewidth=2.5)
    # Head
    head = plt.Circle((cx, cy + 2.1), 0.25, facecolor='#FFE0B2',
                       edgecolor='#333333', linewidth=2)
    ax.add_patch(head)
    # Smile
    smile = mpatches.Arc((cx, cy + 2.05), 0.2, 0.15, angle=0,
                          theta1=200, theta2=340, color='#333333', linewidth=1.5)
    ax.add_patch(smile)

    # Phone in hand
    phone = FancyBboxPatch((cx + 0.55, cy + 1.4), 0.35, 0.5,
                            boxstyle="round,pad=0.03",
                            facecolor='#333333', edgecolor='white', linewidth=1)
    ax.add_patch(phone)
    screen = FancyBboxPatch((cx + 0.59, cy + 1.47), 0.27, 0.32,
                             boxstyle="round,pad=0.01",
                             facecolor=V4_COLORS['MLTEAL'], edgecolor='none')
    ax.add_patch(screen)
    ax.text(cx + 0.725, cy + 1.63, 'PAY', ha='center', va='center',
            fontsize=5, color='white', fontweight='bold')

    # Tap waves from phone
    for r in [0.15, 0.25, 0.35]:
        wave = mpatches.Arc((cx + 0.95, cy + 1.65), r * 2, r * 2,
                             angle=0, theta1=-40, theta2=40,
                             color=V4_COLORS['MLTEAL'], linewidth=1.5, alpha=0.6)
        ax.add_patch(wave)

    # === CASHIER (right side) - confused, holding cash ===
    rx, ry = 8.0, 0.8
    # Legs
    ax.plot([rx, rx - 0.3], [ry, ry + 0.8], color='#333333', linewidth=2.5)
    ax.plot([rx, rx + 0.3], [ry, ry + 0.8], color='#333333', linewidth=2.5)
    # Torso
    ax.plot([rx, rx], [ry + 0.8, ry + 1.8], color='#333333', linewidth=2.5)
    # Arms - left arm holding up cash, right arm shrugging
    ax.plot([rx, rx - 0.7], [ry + 1.5, ry + 1.9], color='#333333', linewidth=2.5)
    ax.plot([rx, rx + 0.5], [ry + 1.5, ry + 1.8], color='#333333', linewidth=2.5)
    # Head
    head2 = plt.Circle((rx, ry + 2.1), 0.25, facecolor='#FFE0B2',
                        edgecolor='#333333', linewidth=2)
    ax.add_patch(head2)
    # Confused expression - squiggle mouth
    ax.plot([rx - 0.08, rx - 0.03, rx + 0.03, rx + 0.08],
            [ry + 2.02, ry + 2.06, ry + 1.98, ry + 2.02],
            color='#333333', linewidth=1.5)
    # Question mark above head
    ax.text(rx + 0.35, ry + 2.5, '?', fontsize=16, fontweight='bold',
            color=V4_COLORS['MLRED'], ha='center', va='center')

    # Cash bill in cashier's left hand
    bill = FancyBboxPatch((rx - 1.05, ry + 1.8), 0.5, 0.25,
                           boxstyle="round,pad=0.02",
                           facecolor=V4_COLORS['MLGREEN'], edgecolor='#333333',
                           linewidth=1, alpha=0.8)
    ax.add_patch(bill)
    ax.text(rx - 0.8, ry + 1.925, '$', ha='center', va='center',
            fontsize=8, fontweight='bold', color='white')

    # Counter/register between them
    counter = Rectangle((5.0, 0.8), 1.8, 0.9,
                         facecolor='#D2B48C', edgecolor='#8B7355', linewidth=2)
    ax.add_patch(counter)
    # Register on counter
    register = FancyBboxPatch((5.3, 1.7), 1.2, 0.5,
                               boxstyle="round,pad=0.05",
                               facecolor='#666666', edgecolor='#444444', linewidth=1.5)
    ax.add_patch(register)
    ax.text(5.9, 1.95, 'POS', ha='center', va='center',
            fontsize=7, fontweight='bold', color='#CCCCCC')

    # Cashier speech bubble
    bubble = FancyBboxPatch((6.5, 4.0), 5.0, 1.5,
                             boxstyle="round,pad=0.2",
                             facecolor='white', edgecolor='#333333', linewidth=1.5)
    ax.add_patch(bubble)
    ax.text(9.0, 4.75, '"Sorry, we don\'t accept...\n  whatever that is."',
            ha='center', va='center', fontsize=10.5, fontstyle='italic',
            color='#333333')
    # Bubble tail
    ax.plot([8.0, 8.1, 8.3], [4.0, 3.5, 4.0], color='#333333', linewidth=1.5)

    # Sign on wall: "CONTACTLESS ONLY"
    sign = FancyBboxPatch((0.5, 4.5), 2.5, 0.8,
                           boxstyle="round,pad=0.1",
                           facecolor=V4_COLORS['MLTEAL'], edgecolor='white',
                           linewidth=1.5, alpha=0.85)
    ax.add_patch(sign)
    ax.text(1.75, 4.9, 'CONTACTLESS\nONLY', ha='center', va='center',
            fontsize=8, fontweight='bold', color='white')

    ax.set_title('The Cashless Future',
                 fontsize=14, fontweight='bold', pad=15, color='#333333')

output_path = os.path.join(os.path.dirname(__file__), 'cartoon.pdf')
save_chart(fig, output_path)
