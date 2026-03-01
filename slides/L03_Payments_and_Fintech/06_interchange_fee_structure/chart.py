"""
Figure 06: Interchange Fee Structure
Fee flow diagram showing who pays whom in a card transaction:
interchange fee, assessment fee, processing fee.
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
    'title': 'Interchange Fee Structure',
    'type': 'flowchart',
    'section': 'Payment Economics',
    'lecture_number': 3,
}

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')
fig.patch.set_facecolor('white')

# --- Entity boxes ---
entities = {
    'Merchant':       (1.5, 5.5, V4_COLORS['MLORANGE']),
    'Acquirer':       (4.0, 5.5, V4_COLORS['MLPURPLE']),
    'Card\nNetwork':  (6.5, 5.5, V4_COLORS['MLRED']),
    'Issuing\nBank':  (9.0, 5.5, V4_COLORS['MLTEAL']),
}

bw, bh = 1.8, 0.9
for label, (cx, cy, color) in entities.items():
    box = FancyBboxPatch((cx - bw / 2, cy - bh / 2), bw, bh,
                          boxstyle="round,pad=0.1",
                          facecolor=color, edgecolor='white', linewidth=2, alpha=0.92)
    ax.add_patch(box)
    ax.text(cx, cy, label, ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')

# --- Fee flow arrows ---
arrow_kw = dict(arrowstyle='->', lw=2.5, connectionstyle='arc3,rad=0.0')

# Merchant -> Acquirer: Merchant Discount Rate
ax.annotate('', xy=(3.0, 5.5), xytext=(2.45, 5.5),
            arrowprops=dict(**arrow_kw, color=V4_COLORS['MLORANGE']))
ax.text(2.7, 6.15, 'Merchant\nDiscount Rate\n(~2.5%)', ha='center', va='center',
        fontsize=7.5, fontweight='bold', color=V4_COLORS['MLORANGE'])

# Acquirer -> Network: Assessment Fee
ax.annotate('', xy=(5.55, 5.5), xytext=(4.95, 5.5),
            arrowprops=dict(**arrow_kw, color=V4_COLORS['MLPURPLE']))
ax.text(5.25, 6.15, 'Assessment\nFee (~0.15%)', ha='center', va='center',
        fontsize=7.5, fontweight='bold', color=V4_COLORS['MLPURPLE'])

# Acquirer -> Issuer: Interchange Fee (long curved arrow below)
ax.annotate('', xy=(8.1, 5.0), xytext=(4.9, 5.0),
            arrowprops=dict(arrowstyle='->', color=V4_COLORS['MLTEAL'], lw=2.5,
                            connectionstyle='arc3,rad=-0.3'))
ax.text(6.5, 3.6, 'Interchange Fee (~1.8%)', ha='center', va='center',
        fontsize=9, fontweight='bold', color=V4_COLORS['MLTEAL'],
        bbox=dict(boxstyle='round,pad=0.3', facecolor=V4_COLORS['MLTEAL'],
                  alpha=0.12, edgecolor=V4_COLORS['MLTEAL'], linewidth=1))

# --- Fee breakdown box ---
breakdown_x, breakdown_y = 5.0, 1.5
bd_w, bd_h = 6.0, 1.8
bd_box = FancyBboxPatch((breakdown_x - bd_w / 2, breakdown_y - bd_h / 2),
                          bd_w, bd_h, boxstyle="round,pad=0.15",
                          facecolor='#F8F8F8', edgecolor='#CCCCCC', linewidth=1.5)
ax.add_patch(bd_box)

ax.text(5.0, 2.2, 'Typical Fee Breakdown on a $100 Transaction (Illustrative)',
        ha='center', va='center', fontsize=9, fontweight='bold', color='#333333')

fees_text = [
    ('Interchange (to Issuer):', '$1.80', V4_COLORS['MLTEAL']),
    ('Assessment (to Network):', '$0.15', V4_COLORS['MLRED']),
    ('Acquirer Markup:',         '$0.55', V4_COLORS['MLPURPLE']),
    ('Total Merchant Cost:',     '$2.50', V4_COLORS['MLORANGE']),
]

for i, (label, amount, color) in enumerate(fees_text):
    y = 1.7 - i * 0.35
    ax.text(3.2, y, label, ha='right', va='center', fontsize=8, color='#555555')
    ax.text(3.4, y, amount, ha='left', va='center', fontsize=8,
            fontweight='bold', color=color)

ax.set_title('Card Payment Fee Structure (Illustrative)',
             fontsize=14, fontweight='bold', pad=15, color='#333333')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
