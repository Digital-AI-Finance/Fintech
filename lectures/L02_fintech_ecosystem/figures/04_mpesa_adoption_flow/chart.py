"""
Figure 04: M-Pesa Adoption Flow
Flowchart showing Safaricom -> Agent Network -> M-Pesa Account -> Services.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '_shared'))

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
    'title': 'M-Pesa Adoption Flow',
    'type': 'flowchart',
    'section': 'Case Study: M-Pesa',
    'lecture_number': 2,
}

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')
fig.patch.set_facecolor('white')

def add_box(ax, x, y, w, h, text, color, fontsize=10, subtext=None):
    box = FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                          boxstyle="round,pad=0.15",
                          facecolor=color, edgecolor='white',
                          linewidth=2, alpha=0.92)
    ax.add_patch(box)
    if subtext:
        ax.text(x, y + 0.08, text, ha='center', va='center',
                fontsize=fontsize, fontweight='bold', color='white')
        ax.text(x, y - 0.15, subtext, ha='center', va='center',
                fontsize=7, color='white', alpha=0.85)
    else:
        ax.text(x, y, text, ha='center', va='center',
                fontsize=fontsize, fontweight='bold', color='white')

def add_arrow(ax, x1, y1, x2, y2):
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                             arrowstyle='->', mutation_scale=18,
                             color='#888888', linewidth=2)
    ax.add_patch(arrow)

# Layer 1: Safaricom
add_box(ax, 5, 5.2, 3.5, 0.6, 'Safaricom', V4_COLORS['MLPURPLE'], fontsize=13,
        subtext='Telecom Operator')

# Arrow
add_arrow(ax, 5, 4.85, 5, 4.3)

# Layer 2: Agent Network
add_box(ax, 5, 3.95, 3.5, 0.6, 'Agent Network', V4_COLORS['MLORANGE'], fontsize=12,
        subtext='100,000+ Shops Nationwide')

# Arrow
add_arrow(ax, 5, 3.6, 5, 3.05)

# Layer 3: M-Pesa Account
add_box(ax, 5, 2.7, 3.5, 0.6, 'M-Pesa Account', V4_COLORS['MLTEAL'], fontsize=12,
        subtext='33M+ Active Users')

# Arrows from M-Pesa to services
service_xs = [1.5, 3.1, 4.7, 6.3, 7.9, 9.5]
service_labels = ['P2P\nTransfer', 'Bill\nPayment', 'Merchant\nPayment',
                  'Savings\n(M-Shwari)', 'Credit\n(KCB)', 'Insurance']

# Fan arrows from center to services
for sx in service_xs:
    add_arrow(ax, 5, 2.35, sx, 1.45)

# Layer 4: 6 services
for sx, label in zip(service_xs, service_labels):
    add_box(ax, sx, 1.05, 1.35, 0.7, label, V4_COLORS['MLGREEN'], fontsize=8)

ax.set_title('M-Pesa Adoption Flow: From Telecom to Financial Platform',
             fontsize=14, fontweight='bold', pad=15, color='#333333')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
