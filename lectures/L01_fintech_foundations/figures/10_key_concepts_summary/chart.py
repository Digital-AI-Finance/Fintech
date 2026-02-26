"""
Figure 10: Key Concepts Summary Table
Summary reference card with 7 concepts, purple header, alternating row backgrounds.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '_shared'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

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
    'title': 'Key Concepts Summary',
    'type': 'summary_table',
    'section': 'SOWHAT',
    'lecture_number': 1,
}

concepts = [
    ('Fintech Definition',
     'Technology-enabled innovation creating new financial products, processes, or business models.'),
    ('Historical Evolution',
     'From credit cards (1950s) through internet banking (1990s) to embedded finance (2020s).'),
    ('Crisis Catalyst',
     'The 2008 crisis eroded trust, opened regulatory space, and released talent for fintech.'),
    ('Value Chain Unbundling',
     'Fintechs attack specific banking layers (origination, distribution, servicing) not the whole bank.'),
    ('Collaboration Models',
     'Partnership, Acquisition, White-Label, Open Banking \u2014 each with distinct trade-offs.'),
    ('Global Patterns',
     'Adoption highest where traditional banking is weakest: the "leapfrog effect" (M-Pesa, PIX).'),
    ('Evaluation Framework',
     'Five questions: customer, value chain layer, revenue model, regulatory position, value creation.'),
]

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Main title
ax.text(5.0, 5.72, 'Lecture 1: Key Concepts at a Glance',
        fontsize=14, fontweight='bold', ha='center', va='center', color='#333333')

# Header row
header_h = 0.42
header_y = 5.18
header_box = FancyBboxPatch((0.25, header_y - header_h / 2), 9.5, header_h,
                             boxstyle='round,pad=0.05', facecolor=V4_COLORS['MLPURPLE'],
                             edgecolor='white', linewidth=1.2, alpha=0.95, zorder=3)
ax.add_patch(header_box)
ax.text(2.5, header_y, 'CONCEPT', ha='center', va='center',
        fontsize=9.5, fontweight='bold', color='white', zorder=4)
ax.text(6.8, header_y, 'ONE-SENTENCE SUMMARY', ha='center', va='center',
        fontsize=9.5, fontweight='bold', color='white', zorder=4)
# Vertical divider in header
ax.plot([4.2, 4.2], [header_y - header_h / 2, header_y + header_h / 2],
        color='white', linewidth=0.8, zorder=4)

# Data rows
n_rows = len(concepts)
row_h = 0.60
total_table_h = n_rows * row_h
start_y = header_y - header_h / 2 - row_h

row_colors = ['#F5F0FA', '#FFFFFF']  # alternating: light purple tint / white

for i, (concept, summary) in enumerate(concepts):
    ry = start_y - i * row_h
    fc = row_colors[i % 2]
    row_box = FancyBboxPatch((0.25, ry - row_h / 2), 9.5, row_h,
                              boxstyle='square,pad=0', facecolor=fc,
                              edgecolor='#E0E0E0', linewidth=0.5, alpha=1.0, zorder=2)
    ax.add_patch(row_box)

    # Concept name (left column)
    ax.text(0.45, ry, concept, ha='left', va='center',
            fontsize=8.5, color=V4_COLORS['MLPURPLE'], fontweight='bold', zorder=3)

    # Vertical divider
    ax.plot([4.2, 4.2], [ry - row_h / 2, ry + row_h / 2],
            color='#DDDDDD', linewidth=0.8, zorder=3)

    # Summary text (right column)
    ax.text(4.35, ry, summary, ha='left', va='center',
            fontsize=8.0, color='#333333', zorder=3,
            wrap=True)

# Bottom border line
bottom_y = start_y - n_rows * row_h + row_h / 2
ax.plot([0.25, 9.75], [bottom_y, bottom_y], color='#CCCCCC', linewidth=0.8)

ax.text(5.0, 0.22, 'Apply these concepts to evaluate any fintech company you encounter in this course.',
        fontsize=8, ha='center', va='center', color='#888888', style='italic')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
