"""
Figure 01: Fintech Ecosystem Map
Central hub with inner ring of key players and outer ring of customer segments.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '_shared'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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
    'title': 'Fintech Ecosystem Map',
    'type': 'ecosystem_diagram',
    'section': 'The Fintech Ecosystem',
    'lecture_number': 2,
}

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.set_xlim(-1.6, 1.6)
ax.set_ylim(-1.1, 1.1)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_facecolor('white')

# Central hub
hub = mpatches.FancyBboxPatch((-0.32, -0.12), 0.64, 0.24,
                               boxstyle="round,pad=0.05",
                               facecolor=V4_COLORS['MLTEAL'], edgecolor='white',
                               linewidth=2, alpha=0.95)
ax.add_patch(hub)
ax.text(0, 0, 'Fintech\nServices', ha='center', va='center',
        fontsize=12, fontweight='bold', color='white')

# Inner ring: 6 nodes
inner_r = 0.55
inner_labels = ['Startups', 'Banks', 'BigTech', 'Regulators', 'Investors', 'Tech\nProviders']
inner_colors = [V4_COLORS['MLORANGE'], V4_COLORS['MLBLUE'], V4_COLORS['MLPURPLE'],
                V4_COLORS['MLRED'], V4_COLORS['MLGREEN'], V4_COLORS['MLCYAN']]

inner_positions = []
for i, (label, color) in enumerate(zip(inner_labels, inner_colors)):
    angle = np.pi / 2 + 2 * np.pi * i / 6
    x = inner_r * np.cos(angle)
    y = inner_r * np.sin(angle)
    inner_positions.append((x, y))
    box = mpatches.FancyBboxPatch((x - 0.2, y - 0.09), 0.4, 0.18,
                                   boxstyle="round,pad=0.03",
                                   facecolor=color, edgecolor='white',
                                   linewidth=1.5, alpha=0.9)
    ax.add_patch(box)
    ax.text(x, y, label, ha='center', va='center',
            fontsize=8, fontweight='bold', color='white')
    # Arrow from hub to inner node
    dx = x * 0.35
    dy = y * 0.35
    ax.annotate('', xy=(x - (x - dx) * 0.45, y - (y - dy) * 0.45),
                xytext=(dx * 0.6, dy * 0.6),
                arrowprops=dict(arrowstyle='->', color='#AAAAAA', lw=1.2,
                                connectionstyle='arc3,rad=0.0'))

# Outer ring: 4 customer segments
outer_r = 1.05
outer_labels = ['Banked\nConsumers', 'Unbanked\nConsumers', 'SMBs', 'Enterprises']
outer_colors = [V4_COLORS['MLGREEN'], V4_COLORS['MLORANGE'], V4_COLORS['MLBLUE'], V4_COLORS['MLPURPLE']]
outer_angles = [np.pi / 2, np.pi, 3 * np.pi / 2, 0]

for label, color, angle in zip(outer_labels, outer_colors, outer_angles):
    x = outer_r * np.cos(angle)
    y = outer_r * np.sin(angle)
    box = mpatches.FancyBboxPatch((x - 0.22, y - 0.1), 0.44, 0.2,
                                   boxstyle="round,pad=0.04",
                                   facecolor='white', edgecolor=color,
                                   linewidth=2.5, alpha=0.95)
    ax.add_patch(box)
    ax.text(x, y, label, ha='center', va='center',
            fontsize=8, fontweight='bold', color=color)
    # Dashed arrow from outer to hub direction
    dx = x * 0.25
    dy = y * 0.25
    ax.annotate('', xy=(dx * 0.8, dy * 0.8),
                xytext=(x - (x - dx) * 0.35, y - (y - dy) * 0.35),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.5,
                                linestyle='dashed',
                                connectionstyle='arc3,rad=0.0'))

ax.set_title('Fintech Ecosystem Map', fontsize=14, fontweight='bold',
             pad=15, color='#333333')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
