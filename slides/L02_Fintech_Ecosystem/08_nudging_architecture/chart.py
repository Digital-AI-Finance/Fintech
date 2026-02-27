"""
Figure 08: Nudging Architecture
3-layer architecture diagram: Design Choices -> Decision Environment -> User Behaviors + Ethical Filter.
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
    'title': 'Nudging Architecture',
    'type': 'architecture_diagram',
    'section': 'Behavioral Design',
    'lecture_number': 2,
}

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6.5)
ax.axis('off')
fig.patch.set_facecolor('white')

def add_box(ax, x, y, w, h, text, color, fontsize=9, alpha=0.92):
    box = FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                          boxstyle="round,pad=0.1",
                          facecolor=color, edgecolor='white',
                          linewidth=1.5, alpha=alpha)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center',
            fontsize=fontsize, fontweight='bold', color='white')

# Layer 1 (top): 5 Design Choices boxes
ax.text(5, 6.2, 'DESIGN CHOICES', ha='center', va='center',
        fontsize=11, fontweight='bold', color='#555555')
design_labels = ['Defaults', 'Framing', 'Social\nProof', 'Commitment', 'Simplification']
design_xs = [1.3, 3.15, 5.0, 6.85, 8.7]
for lbl, dx in zip(design_labels, design_xs):
    add_box(ax, dx, 5.5, 1.5, 0.65, lbl, V4_COLORS['MLPURPLE'], fontsize=8)

# Arrows from design choices to decision environment
for dx in design_xs:
    arrow = FancyArrowPatch((dx, 5.13), (dx, 4.22),
                             arrowstyle='->', mutation_scale=14,
                             color=V4_COLORS['MLGREEN'], linewidth=1.5)
    ax.add_patch(arrow)

# Layer 2 (middle): Decision Environment
env_box = FancyBboxPatch((1.0, 3.55), 8.0, 0.8,
                          boxstyle="round,pad=0.15",
                          facecolor=V4_COLORS['MLTEAL'], edgecolor='white',
                          linewidth=2, alpha=0.92)
ax.add_patch(env_box)
ax.text(5, 3.95, 'DECISION ENVIRONMENT', ha='center', va='center',
        fontsize=12, fontweight='bold', color='white')

# Arrows from decision env to behaviors (green solid for beneficial)
behavior_xs = [2.0, 4.0, 6.0, 8.0]
behavior_labels = ['Saving', 'Investing', 'Borrowing', 'Insuring']

for bx in behavior_xs:
    # Beneficial green arrow
    arrow = FancyArrowPatch((bx, 3.5), (bx, 2.62),
                             arrowstyle='->', mutation_scale=14,
                             color=V4_COLORS['MLGREEN'], linewidth=2)
    ax.add_patch(arrow)

# Some red dashed arrows for harmful paths
for bx in [3.0, 7.0]:
    arrow = FancyArrowPatch((bx, 3.5), (bx, 2.62),
                             arrowstyle='->', mutation_scale=14,
                             color=V4_COLORS['MLRED'], linewidth=1.5,
                             linestyle='dashed')
    ax.add_patch(arrow)

# Layer 3 (bottom): 4 User Behaviors
ax.text(5, 1.65, 'USER BEHAVIORS', ha='center', va='center',
        fontsize=11, fontweight='bold', color='#555555')
for lbl, bx in zip(behavior_labels, behavior_xs):
    add_box(ax, bx, 2.2, 1.5, 0.6, lbl, V4_COLORS['MLBLUE'], fontsize=10)

# Side: Ethical Filter box
filter_box = FancyBboxPatch((0.0, 2.8), 0.8, 2.2,
                             boxstyle="round,pad=0.1",
                             facecolor=V4_COLORS['MLGREEN'], edgecolor='white',
                             linewidth=2, alpha=0.9)
ax.add_patch(filter_box)
ax.text(0.4, 3.9, 'E\nT\nH\nI\nC\nA\nL\n\nF\nI\nL\nT\nE\nR', ha='center', va='center',
        fontsize=6, fontweight='bold', color='white', linespacing=0.7)

# Legend
legend_elements = [
    mpatches.Patch(facecolor=V4_COLORS['MLGREEN'], label='Beneficial path'),
    mpatches.Patch(facecolor=V4_COLORS['MLRED'], label='Harmful path (filtered)'),
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=8,
          frameon=True, facecolor='white', edgecolor='#CCCCCC')

ax.set_title('Choice Architecture: Nudging in Fintech',
             fontsize=14, fontweight='bold', pad=15, color='#333333')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
