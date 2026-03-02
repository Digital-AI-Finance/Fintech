"""
Figure 08: Regulatory Sandbox Adoption Timeline
Timeline from 2016-2025 with event markers for sandbox launches across
jurisdictions, plus a cumulative count line overlay.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '_shared'))

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
    'title': 'Regulatory Sandbox Adoption Timeline',
    'type': 'time_series',
    'section': 'Regulatory Innovation',
    'lecture_number': 4,
}

np.random.seed(42)

# Sandbox launch events
events = [
    (2016.0, 'UK FCA',            V4_COLORS['MLBLUE']),
    (2016.5, 'Singapore MAS',     V4_COLORS['MLTEAL']),
    (2017.0, 'Australia ASIC',    V4_COLORS['MLORANGE']),
    (2017.3, 'Hong Kong HKMA',    V4_COLORS['MLRED']),
    (2018.0, 'Bahrain CBB',       V4_COLORS['MLPURPLE']),
    (2018.4, 'Canada CSA',        V4_COLORS['MLGREEN']),
    (2018.8, 'Arizona (US)',      V4_COLORS['MLBROWN']),
    (2019.0, 'EU (Lithuania)',    V4_COLORS['MLBLUE']),
    (2019.5, 'Thailand SEC',      V4_COLORS['MLORANGE']),
    (2020.0, 'EU (Netherlands)',  V4_COLORS['MLTEAL']),
    (2020.5, 'Saudi Arabia SAMA', V4_COLORS['MLPURPLE']),
    (2021.0, 'India RBI',         V4_COLORS['MLRED']),
    (2021.5, 'Brazil BCB',        V4_COLORS['MLGREEN']),
    (2022.0, 'Nigeria CBN',       V4_COLORS['MLORANGE']),
    (2023.0, 'Wyoming (US)',      V4_COLORS['MLBROWN']),
    (2023.5, 'Kenya CMA',         V4_COLORS['MLPURPLE']),
    (2024.0, 'EU (MiCA sandbox)', V4_COLORS['MLBLUE']),
    (2025.0, 'Various expansions', V4_COLORS['MLGRAY']),
]

years = [e[0] for e in events]
cumulative = list(range(1, len(events) + 1))

fig, ax1 = plt.subplots(1, 1, figsize=(10, 6))
fig.patch.set_facecolor('white')

# Cumulative line
ax1.fill_between(years, cumulative, alpha=0.12, color=V4_COLORS['MLBLUE'])
ax1.plot(years, cumulative, color=V4_COLORS['MLBLUE'], linewidth=2.5,
         marker='o', markersize=4, zorder=3)

# Event markers
for i, (year, name, color) in enumerate(events):
    direction = 1 if i % 2 == 0 else -1
    y_offset = 2.5 * direction if direction > 0 else 1.8 * direction
    y_text = cumulative[i] + y_offset

    ax1.annotate(name,
                 xy=(year, cumulative[i]),
                 xytext=(year, y_text),
                 fontsize=6.5, fontweight='bold', color=color,
                 ha='center', va='center',
                 arrowprops=dict(arrowstyle='->', color=color,
                                 lw=1.0, alpha=0.6),
                 bbox=dict(boxstyle='round,pad=0.2', facecolor=color,
                           alpha=0.1, edgecolor=color, linewidth=0.8))

ax1.set_xlim(2015.5, 2025.5)
ax1.set_ylim(0, 24)

apply_v4_style(ax1, title='Regulatory Sandbox Adoption Around the World',
               xlabel='Year', ylabel='Cumulative Number of Sandboxes')

ax1.yaxis.grid(True, alpha=0.3, linestyle='--')
ax1.set_axisbelow(True)

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
