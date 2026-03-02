"""
Figure 07: RegTech Technology Stack
Five horizontal layers stacked showing the RegTech architecture from
data ingestion through audit, with technology labels per layer.
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
    'title': 'RegTech Technology Stack',
    'type': 'diagram',
    'section': 'RegTech Solutions',
    'lecture_number': 4,
}

np.random.seed(42)

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')
fig.patch.set_facecolor('white')

# Layers from bottom to top
layers = [
    ('DATA INGESTION', 'APIs | Data Feeds | Screen Scraping | Blockchain Listeners',
     V4_COLORS['MLBLUE']),
    ('DATA PROCESSING', 'NLP | ML Pipelines | Entity Resolution | Data Normalization',
     V4_COLORS['MLTEAL']),
    ('ANALYTICS', 'Pattern Detection | Risk Scoring | Anomaly Detection | Graph Analysis',
     V4_COLORS['MLORANGE']),
    ('REPORTING', 'Regulatory Filings | Real-time Dashboards | Alert Management | Audit Reports',
     V4_COLORS['MLPURPLE']),
    ('AUDIT & COMPLIANCE', 'Audit Trail | Evidence Store | Version Control | Regulatory Proofs',
     V4_COLORS['MLRED']),
]

layer_height = 1.0
gap = 0.15
start_y = 0.8
box_left = 1.2
box_width = 7.6

for i, (name, techs, color) in enumerate(layers):
    y = start_y + i * (layer_height + gap)

    # Layer box
    layer_box = FancyBboxPatch((box_left, y), box_width, layer_height,
                                boxstyle="round,pad=0.12",
                                facecolor=color, edgecolor='white',
                                linewidth=2, alpha=0.88)
    ax.add_patch(layer_box)

    # Layer name (left side)
    ax.text(box_left + 0.3, y + layer_height / 2 + 0.12, name,
            ha='left', va='center', fontsize=9.5, fontweight='bold', color='white')

    # Tech labels (below name)
    ax.text(box_left + 0.3, y + layer_height / 2 - 0.18, techs,
            ha='left', va='center', fontsize=7, color='white', alpha=0.85)

    # Layer number
    ax.text(box_left - 0.5, y + layer_height / 2, f'L{i + 1}',
            ha='center', va='center', fontsize=10, fontweight='bold',
            color=color, alpha=0.7)

# Upward arrow on the right side indicating data flow
arrow_x = 9.3
ax.annotate('', xy=(arrow_x, start_y + 5 * (layer_height + gap) - gap),
            xytext=(arrow_x, start_y),
            arrowprops=dict(arrowstyle='->', color='#AAAAAA', lw=2.5))
ax.text(arrow_x, start_y + 2.5 * (layer_height + gap) - gap / 2,
        'Data Flow', ha='center', va='center', fontsize=8, color='#888888',
        rotation=90, fontweight='bold')

# Left side label
ax.text(0.3, start_y + 2.5 * (layer_height + gap) - gap / 2,
        'Abstraction\nLevel', ha='center', va='center', fontsize=8,
        color='#888888', fontweight='bold')
ax.annotate('', xy=(0.3, start_y + 5 * (layer_height + gap) - gap),
            xytext=(0.3, start_y),
            arrowprops=dict(arrowstyle='<->', color='#CCCCCC', lw=1.5))

ax.set_title('RegTech Technology Stack',
             fontsize=14, fontweight='bold', pad=15, color='#333333')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
