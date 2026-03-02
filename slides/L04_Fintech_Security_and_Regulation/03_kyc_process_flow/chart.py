"""
Figure 03: KYC Process Lifecycle
Vertical flowchart depicting the Know Your Customer lifecycle from application
through ongoing monitoring, with manual vs. digital verification branches.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '_shared'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
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
    def save_chart(fig, filename='chart.pdf', dpi=300):
        fig.tight_layout()
        fig.savefig(filename, format='pdf', bbox_inches='tight', dpi=dpi, facecolor='white')
        plt.close(fig)
        print(f'Saved: {filename}')

CHART_METADATA = {
    'title': 'KYC Process Lifecycle',
    'type': 'flowchart',
    'section': 'AML/KYC Compliance',
    'lecture_number': 4,
}

np.random.seed(42)

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')
fig.patch.set_facecolor('white')

# Main flow (center column)
main_steps = [
    ('Application\nSubmitted',        5.0, 7.2, V4_COLORS['MLBLUE']),
    ('Document\nCollection',          5.0, 6.1, V4_COLORS['MLBLUE']),
    ('PEP / Sanctions\nScreening',    5.0, 3.6, V4_COLORS['MLORANGE']),
    ('Risk\nRating',                  5.0, 2.5, V4_COLORS['MLORANGE']),
    ('Ongoing\nMonitoring',           5.0, 1.4, V4_COLORS['MLTEAL']),
    ('Periodic\nReview',              5.0, 0.3, V4_COLORS['MLTEAL']),
]

# Branch steps (verification)
branch_steps = [
    ('Manual\nVerification',   2.8, 4.85, V4_COLORS['MLRED']),
    ('Digital / eKYC\nVerification', 7.2, 4.85, V4_COLORS['MLGREEN']),
]

box_w, box_h = 1.6, 0.7
arrow_kw = dict(arrowstyle='->', color='#555555', lw=1.8)

# Draw main boxes
for label, cx, cy, color in main_steps:
    box = FancyBboxPatch((cx - box_w / 2, cy - box_h / 2), box_w, box_h,
                          boxstyle="round,pad=0.1",
                          facecolor=color, edgecolor='white', linewidth=2, alpha=0.90)
    ax.add_patch(box)
    ax.text(cx, cy, label, ha='center', va='center',
            fontsize=8, fontweight='bold', color='white')

# Draw branch boxes
for label, cx, cy, color in branch_steps:
    box = FancyBboxPatch((cx - box_w / 2, cy - box_h / 2), box_w, box_h,
                          boxstyle="round,pad=0.1",
                          facecolor=color, edgecolor='white', linewidth=2, alpha=0.90)
    ax.add_patch(box)
    ax.text(cx, cy, label, ha='center', va='center',
            fontsize=8, fontweight='bold', color='white')

# Vertical arrows in main column
main_pairs = [(0, 1)]  # Application -> Document Collection
for s, e in main_pairs:
    ax.annotate('', xy=(5.0, main_steps[e][2] + box_h / 2 + 0.02),
                xytext=(5.0, main_steps[s][2] - box_h / 2 - 0.02),
                arrowprops=arrow_kw)

# Document Collection -> branch split
# Left branch
ax.plot([5.0, 5.0], [6.1 - box_h / 2 - 0.02, 5.35], color='#555555', lw=1.8)
ax.plot([5.0, 2.8], [5.35, 5.35], color='#555555', lw=1.8)
ax.annotate('', xy=(2.8, 4.85 + box_h / 2 + 0.02), xytext=(2.8, 5.35),
            arrowprops=arrow_kw)
ax.text(3.7, 5.5, 'Manual', ha='center', fontsize=7, color=V4_COLORS['MLRED'],
        fontstyle='italic')

# Right branch
ax.plot([5.0, 7.2], [5.35, 5.35], color='#555555', lw=1.8)
ax.annotate('', xy=(7.2, 4.85 + box_h / 2 + 0.02), xytext=(7.2, 5.35),
            arrowprops=arrow_kw)
ax.text(6.3, 5.5, 'Digital', ha='center', fontsize=7, color=V4_COLORS['MLGREEN'],
        fontstyle='italic')

# Branches converge back to PEP/Sanctions Screening
ax.plot([2.8, 2.8], [4.85 - box_h / 2 - 0.02, 4.1], color='#555555', lw=1.8)
ax.plot([2.8, 5.0], [4.1, 4.1], color='#555555', lw=1.8)
ax.plot([7.2, 7.2], [4.85 - box_h / 2 - 0.02, 4.1], color='#555555', lw=1.8)
ax.plot([7.2, 5.0], [4.1, 4.1], color='#555555', lw=1.8)
ax.annotate('', xy=(5.0, 3.6 + box_h / 2 + 0.02), xytext=(5.0, 4.1),
            arrowprops=arrow_kw)

# Remaining vertical arrows
for i in range(2, len(main_steps) - 1):
    ax.annotate('', xy=(5.0, main_steps[i + 1][2] + box_h / 2 + 0.02),
                xytext=(5.0, main_steps[i][2] - box_h / 2 - 0.02),
                arrowprops=arrow_kw)

# Feedback loop: Periodic Review -> Ongoing Monitoring
ax.annotate('', xy=(5.0 + box_w / 2 + 0.4, 1.4),
            xytext=(5.0 + box_w / 2 + 0.4, 0.3),
            arrowprops=dict(arrowstyle='->', color=V4_COLORS['MLTEAL'],
                            lw=1.5, linestyle='dashed',
                            connectionstyle='arc3,rad=-0.3'))
ax.text(6.7, 0.85, 'Cycle', ha='center', fontsize=7,
        color=V4_COLORS['MLTEAL'], fontstyle='italic')

# Timing annotations
timings = [
    (0.7, 7.2,  '~5 min'),
    (0.7, 6.1,  '~10 min'),
    (0.7, 4.85, '1-5 days (manual)\n~30 sec (digital)'),
    (0.7, 3.6,  '~1 min'),
    (0.7, 2.5,  '~2 min'),
    (0.7, 1.4,  'Continuous'),
    (0.7, 0.3,  '1-3 years'),
]
for x, y, t in timings:
    ax.text(x, y, t, ha='center', va='center', fontsize=6.5,
            color='#888888', fontstyle='italic')

ax.set_title('KYC Process Lifecycle',
             fontsize=14, fontweight='bold', pad=15, color='#333333')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
