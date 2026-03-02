"""
Figure 12: Closing Cartoon - SupTech vs. Traditional Supervision
XKCD-style cartoon: Two regulators side by side -- human with magnifying glass
examining one transaction, AI on multiple screens monitoring millions.
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
    'title': 'SupTech vs. Traditional Supervision',
    'type': 'cartoon',
    'section': 'Closing',
    'lecture_number': 4,
}

with plt.xkcd():
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis('off')
    fig.patch.set_facecolor('white')

    # Ground line
    ax.plot([0, 12], [0.6, 0.6], color='#888888', linewidth=1.5)

    # Divider
    ax.plot([6, 6], [0.6, 5.5], color='#CCCCCC', linewidth=1.5, linestyle='--')
    ax.text(3.0, 6.5, 'Traditional Supervision', ha='center', va='center',
            fontsize=10, fontweight='bold', color=V4_COLORS['MLBROWN'])
    ax.text(9.0, 6.5, 'SupTech (AI-Powered)', ha='center', va='center',
            fontsize=10, fontweight='bold', color=V4_COLORS['MLTEAL'])

    # ===== LEFT SIDE: Human regulator =====
    hx, hy = 3.0, 0.6

    # Desk
    desk_l = Rectangle((1.5, hy), 3.0, 0.5,
                         facecolor='#D2B48C', edgecolor='#8B7355', linewidth=2)
    ax.add_patch(desk_l)

    # Person behind desk
    # Legs (hidden behind desk)
    # Torso
    ax.plot([hx, hx], [hy + 0.5, hy + 1.5], color='#333333', linewidth=2.5)
    # Arms - right arm holding magnifying glass
    ax.plot([hx, hx - 0.5], [hy + 1.2, hy + 0.8], color='#333333', linewidth=2.5)
    ax.plot([hx, hx + 0.8], [hy + 1.2, hy + 1.5], color='#333333', linewidth=2.5)
    # Head
    head = plt.Circle((hx, hy + 1.8), 0.25, facecolor='#FFE0B2',
                       edgecolor='#333333', linewidth=2)
    ax.add_patch(head)
    # Smile
    smile = mpatches.Arc((hx, hy + 1.73), 0.2, 0.12, angle=0,
                           theta1=200, theta2=340, color='#333333', linewidth=1.5)
    ax.add_patch(smile)

    # Magnifying glass
    glass = plt.Circle((hx + 1.1, hy + 1.7), 0.3, facecolor='none',
                         edgecolor='#333333', linewidth=2.5)
    ax.add_patch(glass)
    # Glass handle
    ax.plot([hx + 0.85, hx + 0.65], [hy + 1.5, hy + 1.3], color='#333333', linewidth=2.5)
    # Glass shine
    ax.plot([hx + 1.0, hx + 1.05], [hy + 1.8, hy + 1.85],
            color=V4_COLORS['MLCYAN'], linewidth=2, alpha=0.6)

    # Single document on desk
    doc = Rectangle((2.0, hy + 0.55), 0.8, 0.5,
                      facecolor='#FAFAFA', edgecolor='#CCCCCC', linewidth=1.2)
    ax.add_patch(doc)
    ax.plot([2.1, 2.6], [hy + 0.85, hy + 0.85], color='#DDDDDD', linewidth=1)
    ax.plot([2.1, 2.5], [hy + 0.75, hy + 0.75], color='#DDDDDD', linewidth=1)
    ax.plot([2.1, 2.6], [hy + 0.65, hy + 0.65], color='#DDDDDD', linewidth=1)

    # Speech bubble (human)
    bubble_h = FancyBboxPatch((0.3, 3.6), 3.5, 1.2,
                               boxstyle="round,pad=0.2",
                               facecolor='white', edgecolor='#333333', linewidth=1.5)
    ax.add_patch(bubble_h)
    ax.text(2.05, 4.2, '"I found a suspicious\n       pattern!"',
            ha='center', va='center', fontsize=9.5, fontstyle='italic',
            color='#333333')
    ax.plot([2.5, 2.8, 2.7], [3.6, 2.8, 3.6], color='#333333', linewidth=1.5)

    # ===== RIGHT SIDE: AI system =====
    rx, ry = 9.0, 0.6

    # Desk/console
    desk_r = Rectangle((7.0, ry), 4.0, 0.5,
                         facecolor='#555555', edgecolor='#444444', linewidth=2)
    ax.add_patch(desk_r)

    # Multiple screens (3 monitors)
    screen_positions = [(7.3, ry + 0.6), (8.6, ry + 0.6), (9.9, ry + 0.6)]
    for sx, sy in screen_positions:
        # Monitor frame
        monitor = FancyBboxPatch((sx, sy), 1.0, 0.9,
                                  boxstyle="round,pad=0.05",
                                  facecolor='#222222', edgecolor='#444444',
                                  linewidth=1.5)
        ax.add_patch(monitor)
        # Screen
        screen = FancyBboxPatch((sx + 0.05, sy + 0.05), 0.9, 0.7,
                                  boxstyle="round,pad=0.02",
                                  facecolor=V4_COLORS['MLTEAL'],
                                  edgecolor='none', alpha=0.8)
        ax.add_patch(screen)
        # Data visualization lines on screen
        for line_y in [sy + 0.2, sy + 0.35, sy + 0.5, sy + 0.65]:
            ax.plot([sx + 0.1, sx + 0.85],
                    [line_y, line_y + np.random.uniform(-0.05, 0.05)],
                    color='white', linewidth=0.8, alpha=0.7)
        # Monitor stand
        ax.plot([sx + 0.5, sx + 0.5], [sy, sy - 0.05], color='#444444', linewidth=2)

    # Robot/AI indicator on middle screen
    ax.text(9.1, ry + 1.0, 'AI', ha='center', va='center',
            fontsize=8, fontweight='bold', color='white')

    # Glowing status lights
    for i, (sx, _) in enumerate(screen_positions):
        status_color = V4_COLORS['MLGREEN'] if i != 1 else V4_COLORS['MLRED']
        ax.plot(sx + 0.5, ry + 1.55, 'o', color=status_color, markersize=3)

    # Data stream arrows flowing into screens
    for sx, sy in screen_positions:
        ax.annotate('', xy=(sx + 0.5, sy + 0.95),
                    xytext=(sx + 0.5, sy + 1.3),
                    arrowprops=dict(arrowstyle='->', color=V4_COLORS['MLCYAN'],
                                    lw=1.2, alpha=0.5))

    # Cloud of data above
    cloud = FancyBboxPatch((7.5, 2.7), 3.0, 0.6,
                            boxstyle="round,pad=0.15",
                            facecolor=V4_COLORS['MLCYAN'], edgecolor='white',
                            linewidth=1.5, alpha=0.2)
    ax.add_patch(cloud)
    ax.text(9.0, 3.0, '47M transactions/day', ha='center', va='center',
            fontsize=7, color=V4_COLORS['MLTEAL'], fontweight='bold')

    # Speech bubble (AI)
    bubble_a = FancyBboxPatch((7.5, 3.8), 4.0, 1.2,
                               boxstyle="round,pad=0.2",
                               facecolor='white', edgecolor='#333333', linewidth=1.5)
    ax.add_patch(bubble_a)
    ax.text(9.5, 4.4, '"I found 47,000."',
            ha='center', va='center', fontsize=10.5, fontstyle='italic',
            color=V4_COLORS['MLTEAL'], fontweight='bold')
    ax.plot([9.0, 9.0, 9.2], [3.8, 3.3, 3.8], color='#333333', linewidth=1.5)

    # Caption at bottom
    ax.text(6.0, 0.15,
            'SupTech vs. Traditional Supervision',
            ha='center', va='center', fontsize=12, fontweight='bold',
            color='#555555', fontstyle='italic')

    ax.set_title('SupTech vs. Traditional Supervision',
                 fontsize=14, fontweight='bold', pad=15, color='#333333')

output_path = os.path.join(os.path.dirname(__file__), 'cartoon.pdf')
save_chart(fig, output_path)
