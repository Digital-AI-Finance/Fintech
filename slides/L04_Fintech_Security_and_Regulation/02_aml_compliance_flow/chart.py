"""
Figure 02: AML Compliance Pipeline
Horizontal flowchart showing the anti-money laundering compliance pipeline
from customer onboarding through SAR filing to case management.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '_shared'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
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
    'title': 'AML Compliance Pipeline',
    'type': 'flowchart',
    'section': 'AML/KYC Compliance',
    'lecture_number': 4,
}

np.random.seed(42)

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')
fig.patch.set_facecolor('white')

# Pipeline stages with phase coloring
stages = [
    ('Customer\nOnboarding',     1.2, 5.0, V4_COLORS['MLBLUE']),
    ('Identity\nVerification',   2.8, 5.0, V4_COLORS['MLBLUE']),
    ('Risk\nScoring',            4.4, 5.0, V4_COLORS['MLORANGE']),
    ('Transaction\nMonitoring',  6.0, 5.0, V4_COLORS['MLORANGE']),
    ('Alert\nReview',            7.6, 5.0, V4_COLORS['MLRED']),
    ('SAR\nFiling',              6.0, 2.5, V4_COLORS['MLRED']),
    ('Case\nManagement',         7.6, 2.5, V4_COLORS['MLRED']),
]

box_w, box_h = 1.3, 0.85

for label, cx, cy, color in stages:
    box = FancyBboxPatch((cx - box_w / 2, cy - box_h / 2), box_w, box_h,
                          boxstyle="round,pad=0.1",
                          facecolor=color, edgecolor='white', linewidth=2, alpha=0.90)
    ax.add_patch(box)
    ax.text(cx, cy, label, ha='center', va='center',
            fontsize=8.5, fontweight='bold', color='white')

# Horizontal arrows along top row
arrow_kw = dict(arrowstyle='->', color='#555555', lw=2)
for i in range(4):
    x_start = stages[i][1] + box_w / 2 + 0.05
    x_end = stages[i + 1][1] - box_w / 2 - 0.05
    y = 5.0
    ax.annotate('', xy=(x_end, y), xytext=(x_start, y), arrowprops=arrow_kw)

# Arrow from Alert Review down to SAR Filing
ax.annotate('', xy=(7.6, 5.0 - box_h / 2 - 0.05),
            xytext=(7.6, 5.0 - box_h / 2 - 0.05),
            arrowprops=arrow_kw)
# Vertical arrow: Alert Review -> Case Management (via a bend)
ax.annotate('', xy=(7.6, 2.5 + box_h / 2 + 0.05),
            xytext=(7.6, 5.0 - box_h / 2 - 0.05),
            arrowprops=dict(arrowstyle='->', color='#555555', lw=2))
# Horizontal arrow: SAR Filing -> Case Management
ax.annotate('', xy=(7.6 - box_w / 2 - 0.05, 2.5),
            xytext=(6.0 + box_w / 2 + 0.05, 2.5),
            arrowprops=arrow_kw)
# Arrow from Transaction Monitoring down to SAR Filing
ax.annotate('', xy=(6.0, 2.5 + box_h / 2 + 0.05),
            xytext=(6.0, 5.0 - box_h / 2 - 0.05),
            arrowprops=dict(arrowstyle='->', color='#555555', lw=2,
                            linestyle='dashed'))

# Phase labels at bottom
phases = [
    ('ONBOARDING', 2.0, 6.4, V4_COLORS['MLBLUE']),
    ('MONITORING', 5.2, 6.4, V4_COLORS['MLORANGE']),
    ('REPORTING', 7.0, 1.3, V4_COLORS['MLRED']),
]
for label, x, y, color in phases:
    ax.text(x, y, label, ha='center', va='center', fontsize=8,
            fontweight='bold', color=color, alpha=0.7,
            bbox=dict(boxstyle='round,pad=0.2', facecolor=color, alpha=0.1,
                      edgecolor=color, linewidth=1))

# Annotation for timing
ax.text(5.0, 0.6, 'Typical end-to-end: 24-72 hours (automated) | weeks (manual review)',
        ha='center', va='center', fontsize=8, color='#888888', fontstyle='italic')

ax.set_title('AML Compliance Pipeline',
             fontsize=14, fontweight='bold', pad=15, color='#333333')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
