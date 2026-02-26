"""
Figure 11: Opening Cartoon (XKCD style)
Banker staring at phone, fintech founder with laptop.
Speech bubbles: "They built this in a weekend?" / "And no branch offices needed!"
Caption: "The revolution started in a garage, not a boardroom."
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '_shared'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np

try:
    from chart_styles import V4_COLORS
except ImportError:
    V4_COLORS = {
        'MLPURPLE': '#9467BD', 'MLBLUE': '#1F77B4', 'MLRED': '#D62728',
        'MLORANGE': '#FF7F0E', 'MLGREEN': '#2CA02C', 'MLGRAY': '#7F7F7F',
        'MLTEAL': '#0D7377', 'MLCYAN': '#14BDEB', 'MLYELLOW': '#BCBD22',
        'MLPINK': '#E377C2', 'MLBROWN': '#8C564B',
    }

CHART_METADATA = {
    'title': 'Opening Cartoon: Fintech Disruption',
    'type': 'cartoon_opening',
    'section': 'WHY',
    'lecture_number': 1,
}

def draw_stick_figure(ax, cx, cy, scale=1.0, color='#333333'):
    """Draw a simple stick figure."""
    head_r = 0.18 * scale
    head = Circle((cx, cy + 0.55 * scale + head_r), head_r,
                   color=color, fill=True, zorder=5)
    ax.add_patch(head)
    # Body
    ax.plot([cx, cx], [cy + 0.55 * scale, cy + 0.15 * scale],
            color=color, lw=2.0 * scale, zorder=5)
    # Arms
    ax.plot([cx - 0.3 * scale, cx + 0.3 * scale],
            [cy + 0.40 * scale, cy + 0.40 * scale],
            color=color, lw=2.0 * scale, zorder=5)
    # Legs
    ax.plot([cx, cx - 0.22 * scale], [cy + 0.15 * scale, cy - 0.18 * scale],
            color=color, lw=2.0 * scale, zorder=5)
    ax.plot([cx, cx + 0.22 * scale], [cy + 0.15 * scale, cy - 0.18 * scale],
            color=color, lw=2.0 * scale, zorder=5)

def draw_speech_bubble(ax, x, y, w, h, text, fontsize=9, tail_x=None, tail_y=None,
                        fc='#FFFDE7', ec='#AAAAAA', style='round,pad=0.15'):
    box = FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                          boxstyle=style, facecolor=fc,
                          edgecolor=ec, linewidth=1.5, zorder=6)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center',
            fontsize=fontsize, color='#222222', zorder=7, wrap=True,
            multialignment='center')
    if tail_x is not None and tail_y is not None:
        ax.plot([x, tail_x], [y - h / 2, tail_y],
                color=ec, lw=1.5, zorder=5)

with plt.xkcd(scale=0.8, length=100, randomness=2):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    fig.patch.set_facecolor('white')

    # Ground line
    ax.axhline(y=1.45, color='#555555', linewidth=1.8, xmin=0.05, xmax=0.95, zorder=3)

    # === LEFT FIGURE: Traditional Banker (suit, holding phone) ===
    banker_cx = 2.5
    draw_stick_figure(ax, banker_cx, 1.45, scale=1.1, color='#333333')

    # Suit jacket lines (visual hint)
    ax.plot([banker_cx - 0.12, banker_cx - 0.28],
            [1.45 + 0.45, 1.45 + 0.15], color='#555555', lw=1.2, zorder=5)
    ax.plot([banker_cx + 0.12, banker_cx + 0.28],
            [1.45 + 0.45, 1.45 + 0.15], color='#555555', lw=1.2, zorder=5)

    # Phone held in right hand
    phone = FancyBboxPatch((banker_cx + 0.28, 1.45 + 0.28), 0.28, 0.42,
                            boxstyle='round,pad=0.03', facecolor='#333333',
                            edgecolor='#111111', linewidth=1.2, zorder=5)
    ax.add_patch(phone)
    ax.text(banker_cx + 0.42, 1.45 + 0.49, '...', ha='center', va='center',
            fontsize=6, color='white', zorder=6)

    # Label
    ax.text(banker_cx, 1.15, 'Traditional\nBanker', ha='center', va='top',
            fontsize=8.5, color='#444444', fontweight='bold')

    # Speech bubble (thought) for banker
    draw_speech_bubble(ax, banker_cx, 4.1, 2.8, 1.05,
                        '"They built this in a\nweekend?!"',
                        fontsize=10, tail_x=banker_cx + 0.1, tail_y=3.0,
                        fc='#EEF4FF', ec=V4_COLORS['MLBLUE'])

    # === RIGHT FIGURE: Fintech Founder (t-shirt, laptop) ===
    founder_cx = 7.5
    draw_stick_figure(ax, founder_cx, 1.45, scale=1.1, color='#333333')

    # Laptop on lap (leaning)
    laptop = FancyBboxPatch((founder_cx - 0.45, 1.45 + 0.05), 0.90, 0.30,
                             boxstyle='round,pad=0.04', facecolor='#AAAAAA',
                             edgecolor='#555555', linewidth=1.0, zorder=5)
    ax.add_patch(laptop)
    ax.text(founder_cx, 1.45 + 0.20, '> python main.py', ha='center', va='center',
            fontsize=5.5, color='#003300', zorder=6, family='monospace')

    # Label
    ax.text(founder_cx, 1.15, 'Fintech\nFounder', ha='center', va='top',
            fontsize=8.5, color='#444444', fontweight='bold')

    # Speech bubble for founder
    draw_speech_bubble(ax, founder_cx, 4.1, 2.8, 1.05,
                        '"And no branch offices\nneeded!"',
                        fontsize=10, tail_x=founder_cx - 0.1, tail_y=3.0,
                        fc='#EFFDE7', ec=V4_COLORS['MLGREEN'])

    # === Central divider / vs label ===
    ax.text(5.0, 2.6, 'vs.', ha='center', va='center',
            fontsize=14, color='#AAAAAA', fontweight='bold')

    # === Caption at bottom ===
    ax.text(5.0, 0.42, '"The revolution started in a garage, not a boardroom."',
            ha='center', va='center', fontsize=11,
            color='#333333', fontstyle='italic', fontweight='bold')

    ax.text(5.0, 0.14, 'This is the tension at the heart of fintech: speed vs. scale, innovation vs. regulation.',
            ha='center', va='center', fontsize=8.0, color='#777777')

    output_path = os.path.join(os.path.dirname(__file__), 'cartoon.pdf')
    fig.tight_layout()
    fig.savefig(output_path, format='pdf', bbox_inches='tight', dpi=300, facecolor='white')
    plt.close(fig)
    print(f'Saved: {output_path}')
