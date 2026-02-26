"""
Figure 04: Fintech Ecosystem Overview
Central hub with 7 inner sector nodes and 5 outer stakeholder nodes.
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
    from chart_styles import V4_COLORS, save_chart
except ImportError:
    V4_COLORS = {
        'MLPURPLE': '#9467BD', 'MLBLUE': '#1F77B4', 'MLRED': '#D62728',
        'MLORANGE': '#FF7F0E', 'MLGREEN': '#2CA02C', 'MLGRAY': '#7F7F7F',
        'MLTEAL': '#0D7377', 'MLCYAN': '#14BDEB', 'MLYELLOW': '#BCBD22',
        'MLPINK': '#E377C2', 'MLBROWN': '#8C564B',
    }
    def save_chart(fig, filename='chart.pdf', dpi=300):
        fig.tight_layout()
        fig.savefig(filename, format='pdf', bbox_inches='tight', dpi=dpi, facecolor='white')
        plt.close(fig)
        print(f'Saved: {filename}')

CHART_METADATA = {
    'title': 'Fintech Ecosystem Overview',
    'type': 'diagram',
    'section': 'WHY',
    'lecture_number': 1,
}

def draw_circle_node(ax, cx, cy, r, color, label, fontsize=8.5, text_color='white', alpha=0.90):
    circle = mpatches.Circle((cx, cy), r, color=color, alpha=alpha, zorder=4)
    ax.add_patch(circle)
    lines = label.split('\n')
    if len(lines) == 1:
        ax.text(cx, cy, label, ha='center', va='center', fontsize=fontsize,
                color=text_color, fontweight='bold', zorder=5)
    else:
        ax.text(cx, cy + r * 0.22, lines[0], ha='center', va='center', fontsize=fontsize,
                color=text_color, fontweight='bold', zorder=5)
        ax.text(cx, cy - r * 0.22, lines[1], ha='center', va='center', fontsize=fontsize - 0.5,
                color=text_color, zorder=5)

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Title
ax.text(5, 5.72, 'The Fintech Ecosystem: Key Players and Relationships',
        fontsize=13, fontweight='bold', ha='center', va='center', color='#333333')

# Central hub
cx, cy = 5.0, 2.9
r_center = 0.62
draw_circle_node(ax, cx, cy, r_center, V4_COLORS['MLPURPLE'],
                 'Financial\nServices', fontsize=8.5)

# Inner ring: 7 sector nodes
inner_sectors = [
    ('Payments', V4_COLORS['MLTEAL']),
    ('Lending', V4_COLORS['MLBLUE']),
    ('Insurance', V4_COLORS['MLORANGE']),
    ('Wealth\nMgmt', V4_COLORS['MLGREEN']),
    ('Capital\nMarkets', V4_COLORS['MLRED']),
    ('RegTech', V4_COLORS['MLPINK']),
    ('Banking\nInfra', V4_COLORS['MLBROWN']),
]
r_inner_orbit = 1.55
r_inner_node = 0.42
n_inner = len(inner_sectors)
for i, (label, color) in enumerate(inner_sectors):
    angle = 2 * np.pi * i / n_inner - np.pi / 2
    ix = cx + r_inner_orbit * np.cos(angle)
    iy = cy + r_inner_orbit * np.sin(angle)
    # Connection line
    ax.plot([cx + r_center * np.cos(angle), ix - r_inner_node * np.cos(angle)],
            [cy + r_center * np.sin(angle), iy - r_inner_node * np.sin(angle)],
            color='#CCCCCC', linewidth=1.1, zorder=2)
    draw_circle_node(ax, ix, iy, r_inner_node, color, label, fontsize=7.5)

# Outer ring: 5 stakeholder nodes
outer_stakeholders = [
    ('Regulators', V4_COLORS['MLGRAY']),
    ('Consumers', V4_COLORS['MLCYAN']),
    ('Investors', V4_COLORS['MLYELLOW']),
    ('Tech\nProviders', V4_COLORS['MLGRAY']),
    ('Incumbents', V4_COLORS['MLGRAY']),
]
r_outer_orbit = 2.65
r_outer_node = 0.30
n_outer = len(outer_stakeholders)
outer_angles = [2 * np.pi * i / n_outer - np.pi / 4 for i in range(n_outer)]
for i, ((label, color), angle) in enumerate(zip(outer_stakeholders, outer_angles)):
    ox = cx + r_outer_orbit * np.cos(angle)
    oy = cy + r_outer_orbit * np.sin(angle)
    # Find nearest inner node to connect to
    inner_angle = 2 * np.pi * (round(angle / (2 * np.pi / n_inner)) % n_inner) / n_inner - np.pi / 2
    ix = cx + r_inner_orbit * np.cos(inner_angle)
    iy = cy + r_inner_orbit * np.sin(inner_angle)
    ax.plot([ix + r_inner_node * np.cos(angle), ox - r_outer_node * np.cos(angle)],
            [iy + r_inner_node * np.sin(angle), oy - r_outer_node * np.sin(angle)],
            color='#DDDDDD', linewidth=0.9, linestyle='--', zorder=1)
    draw_circle_node(ax, ox, oy, r_outer_node, color, label,
                     fontsize=7.0, text_color='white')

ax.text(5.0, 0.22, 'Illustrative ecosystem \u2014 conceptual overview only.',
        fontsize=7.5, ha='center', va='center', color='#888888', style='italic')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
