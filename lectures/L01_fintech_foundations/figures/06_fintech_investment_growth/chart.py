"""
Figure 06: Fintech Investment Growth (Illustrative)
Bar chart 2010-2023 with exponential growth pattern and annotated zones.
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
    'title': 'Fintech Investment Growth (Illustrative)',
    'type': 'comparison_bar',
    'section': 'CASE',
    'lecture_number': 1,
}

years = list(range(2010, 2024))

# Illustrative investment index: exponential growth, dip in 2020, spike 2021, correction 2022-23
values = [
    4,   # 2010
    7,   # 2011
    11,  # 2012
    16,  # 2013
    24,  # 2014
    35,  # 2015
    44,  # 2016
    55,  # 2017
    72,  # 2018
    88,  # 2019
    76,  # 2020 (COVID dip)
    112, # 2021 (boom)
    85,  # 2022 (correction)
    68,  # 2023 (correction)
]

# Zone definitions: (start_year, end_year, label, color, alpha)
zones = [
    (2010, 2013, 'Early Stage', V4_COLORS['MLCYAN'], 0.12),
    (2014, 2017, 'Growth', V4_COLORS['MLGREEN'], 0.12),
    (2018, 2021, 'Boom', V4_COLORS['MLORANGE'], 0.12),
    (2022, 2023, 'Correction', V4_COLORS['MLRED'], 0.12),
]

# Bar colors: gradient from light purple to dark teal
bar_colors = []
n = len(years)
for i in range(n):
    t = i / (n - 1)
    r = int(0x9467BD * (1 - t) + 0x0D7377 * t) >> 16
    # Simpler: blend hex components manually
    r1, g1, b1 = 0x94, 0x67, 0xBD  # MLPURPLE
    r2, g2, b2 = 0x0D, 0x73, 0x77  # MLTEAL
    r = int(r1 * (1 - t) + r2 * t)
    g = int(g1 * (1 - t) + g2 * t)
    b = int(b1 * (1 - t) + b2 * t)
    bar_colors.append(f'#{r:02X}{g:02X}{b:02X}')

fig, ax = plt.subplots(figsize=(10, 6))

# Draw zone shading
for z_start, z_end, z_label, z_color, z_alpha in zones:
    ax.axvspan(z_start - 0.5, z_end + 0.5, alpha=z_alpha, color=z_color, zorder=0)
    ax.text((z_start + z_end) / 2, max(values) * 1.02, z_label,
            ha='center', va='bottom', fontsize=8.5, color=z_color,
            fontweight='bold', style='italic')

# Bars
x_positions = years
bars = ax.bar(x_positions, values, color=bar_colors, edgecolor='white',
              linewidth=0.8, width=0.75, zorder=3)

# Value labels on top of bars
for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width() / 2, val + 1.5,
            str(val), ha='center', va='bottom', fontsize=7, color='#555555')

apply_v4_style(ax,
               title='Illustrative Global Fintech Investment Growth (2010\u20132023)',
               xlabel='Year',
               ylabel='Illustrative Investment Index')

ax.set_xlim(2009.3, 2023.7)
ax.set_ylim(0, 130)
ax.set_xticks(years)
ax.set_xticklabels([str(y) for y in years], rotation=45, ha='right')

# Subtitle note
ax.text(0.5, -0.14, 'Illustrative \u2014 not actual investment data. Conceptual growth trajectory only.',
        transform=ax.transAxes, fontsize=8, color='#888888',
        ha='center', va='center', style='italic')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
