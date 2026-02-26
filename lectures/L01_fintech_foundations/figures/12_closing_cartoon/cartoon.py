"""
Figure 12: Closing Cartoon (XKCD style)
Banker and fintech founder shaking hands, both looking slightly suspicious.
Thought bubbles: "I need their tech." / "I need their license."
Caption: "And that's how partnerships are born."
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '_shared'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

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
    'title': 'Closing Cartoon: Partnership Imperative',
    'type': 'cartoon_closing',
    'section': 'CLOSING',
    'lecture_number': 1,
}

def draw_stick_figure(ax, cx, cy, scale=1.0, color='#333333'):
    head_r = 0.18 * scale
    head = Circle((cx, cy + 0.55 * scale + head_r), head_r,
                   color=color, fill=True, zorder=5)
    ax.add_patch(head)
    ax.plot([cx, cx], [cy + 0.55 * scale, cy + 0.15 * scale],
            color=color, lw=2.0 * scale, zorder=5)
    ax.plot([cx - 0.3 * scale, cx + 0.3 * scale],
            [cy + 0.40 * scale, cy + 0.40 * scale],
            color=color, lw=2.0 * scale, zorder=5)
    ax.plot([cx, cx - 0.22 * scale], [cy + 0.15 * scale, cy - 0.18 * scale],
            color=color, lw=2.0 * scale, zorder=5)
    ax.plot([cx, cx + 0.22 * scale], [cy + 0.15 * scale, cy - 0.18 * scale],
            color=color, lw=2.0 * scale, zorder=5)

def draw_thought_bubble(ax, anchor_x, anchor_y, bubble_x, bubble_y,
                         w, h, text, fontsize=9, fc='#FFFDE7', ec='#AAAAAA'):
    """Thought bubble with dots leading to box."""
    # Three dots from figure head to bubble
    dx = (bubble_x - anchor_x) / 4
    dy = (bubble_y - anchor_y) / 4
    for k in range(1, 4):
        dot_r = 0.035 + k * 0.018
        dot_x = anchor_x + dx * k
        dot_y = anchor_y + dy * k
        dot = Circle((dot_x, dot_y), dot_r, color=ec, fill=True, zorder=5)
        ax.add_patch(dot)
    # Main bubble
    box = FancyBboxPatch((bubble_x - w / 2, bubble_y - h / 2), w, h,
                          boxstyle='round,pad=0.18', facecolor=fc,
                          edgecolor=ec, linewidth=1.5, zorder=6)
    ax.add_patch(box)
    ax.text(bubble_x, bubble_y, text, ha='center', va='center',
            fontsize=fontsize, color='#222222', zorder=7, multialignment='center')

with plt.xkcd(scale=0.8, length=100, randomness=2):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    fig.patch.set_facecolor('white')

    # Ground line
    ax.axhline(y=1.45, color='#555555', linewidth=1.8, xmin=0.05, xmax=0.95, zorder=3)

    # === LEFT FIGURE: Banker ===
    banker_cx = 3.2
    draw_stick_figure(ax, banker_cx, 1.45, scale=1.1, color='#333333')

    # Suit hint
    ax.plot([banker_cx - 0.12, banker_cx - 0.28],
            [1.45 + 0.45, 1.45 + 0.15], color='#555555', lw=1.2, zorder=5)
    ax.plot([banker_cx + 0.12, banker_cx + 0.28],
            [1.45 + 0.45, 1.45 + 0.15], color='#555555', lw=1.2, zorder=5)

    ax.text(banker_cx, 1.15, 'Traditional\nBanker', ha='center', va='top',
            fontsize=8.5, color='#444444', fontweight='bold')

    # Banker thought bubble (upper left)
    draw_thought_bubble(ax,
                         anchor_x=banker_cx, anchor_y=1.45 + 0.55 + 0.18,
                         bubble_x=2.1, bubble_y=4.4,
                         w=2.6, h=0.95,
                         text='"I need their tech."',
                         fontsize=10.5, fc='#EEF4FF', ec=V4_COLORS['MLBLUE'])

    # === RIGHT FIGURE: Fintech Founder ===
    founder_cx = 6.8
    draw_stick_figure(ax, founder_cx, 1.45, scale=1.1, color='#333333')

    # T-shirt hint (no lapels)
    ax.text(founder_cx, 1.45 + 0.30, '[startup\ntee]', ha='center', va='center',
            fontsize=5.5, color='#888888', zorder=5)

    ax.text(founder_cx, 1.15, 'Fintech\nFounder', ha='center', va='top',
            fontsize=8.5, color='#444444', fontweight='bold')

    # Founder thought bubble (upper right)
    draw_thought_bubble(ax,
                         anchor_x=founder_cx, anchor_y=1.45 + 0.55 + 0.18,
                         bubble_x=7.9, bubble_y=4.4,
                         w=2.6, h=0.95,
                         text='"I need their license."',
                         fontsize=10.5, fc='#EFFDE7', ec=V4_COLORS['MLGREEN'])

    # === Handshake in the middle ===
    # Banker's right arm extended
    ax.plot([banker_cx + 0.30 * 1.1, 5.0],
            [1.45 + 0.40 * 1.1, 1.45 + 0.40 * 1.1],
            color='#333333', lw=2.2, zorder=5)
    # Founder's left arm extended
    ax.plot([founder_cx - 0.30 * 1.1, 5.0],
            [1.45 + 0.40 * 1.1, 1.45 + 0.40 * 1.1],
            color='#333333', lw=2.2, zorder=5)
    # Handshake icon (two circles)
    hs = Circle((5.0, 1.45 + 0.40 * 1.1), 0.14, color='#777777', fill=True, zorder=6)
    ax.add_patch(hs)
    ax.text(5.0, 1.45 + 0.40 * 1.1 + 0.25, 'Partnership', ha='center', va='bottom',
            fontsize=8, color='#555555', fontweight='bold')

    # Sideways glance expressions (small curved lines above each head)
    # Banker looking right suspiciously
    ax.plot([banker_cx + 0.06, banker_cx + 0.14], [1.45 + 0.55 + 0.18 * 2 + 0.04,
              1.45 + 0.55 + 0.18 * 2 + 0.04], color='#555555', lw=1.5, zorder=6)
    # Founder looking left suspiciously
    ax.plot([founder_cx - 0.14, founder_cx - 0.06], [1.45 + 0.55 + 0.18 * 2 + 0.04,
              1.45 + 0.55 + 0.18 * 2 + 0.04], color='#555555', lw=1.5, zorder=6)

    # === Caption ===
    ax.text(5.0, 0.52, '"And that\'s how partnerships are born."',
            ha='center', va='center', fontsize=12,
            color='#333333', fontstyle='italic', fontweight='bold')

    ax.text(5.0, 0.18, 'The collaboration imperative: neither side can win alone.',
            ha='center', va='center', fontsize=8.5, color='#777777')

    output_path = os.path.join(os.path.dirname(__file__), 'cartoon.pdf')
    fig.tight_layout()
    fig.savefig(output_path, format='pdf', bbox_inches='tight', dpi=300, facecolor='white')
    plt.close(fig)
    print(f'Saved: {output_path}')
