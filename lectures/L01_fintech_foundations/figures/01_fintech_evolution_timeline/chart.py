"""
Figure 01: Fintech Evolution Timeline
Annotated S-curve from 1950s to 2020s with key milestones.
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
    'title': 'Fintech Evolution Timeline',
    'type': 'time_series',
    'section': 'WHAT',
    'lecture_number': 1,
}

# Milestone data: (year, label, y_value, label_offset_y)
milestones = [
    (1950, 'Credit Cards', 0.08, +0.07),
    (1967, 'ATMs', 0.14, +0.07),
    (1971, 'Electronic Trading\n(NASDAQ)', 0.19, -0.13),
    (1983, 'Online Banking\nExperiments', 0.26, +0.07),
    (1994, 'Internet Banking\n& PayPal', 0.36, -0.13),
    (2003, 'Mobile Banking\nP2P Lending', 0.50, +0.07),
    (2007, 'M-Pesa\n(Mobile Money)', 0.58, -0.13),
    (2008, 'Financial\nCrisis', 0.60, +0.00),
    (2009, 'Bitcoin', 0.63, +0.07),
    (2014, 'Neobanks\nRobo-Advisors\nBNPL', 0.78, -0.15),
    (2018, 'PSD2 / Open\nBanking', 0.86, +0.07),
    (2022, 'Embedded Finance\nDeFi, Super-Apps', 0.96, -0.13),
]

# S-curve backbone
x_fine = np.linspace(1948, 2024, 400)
# Logistic S-curve centered around 1995
y_curve = 1.0 / (1.0 + np.exp(-0.12 * (x_fine - 1995)))
y_curve = y_curve * 0.92 + 0.04  # scale to [0.04, 0.96]

fig, ax = plt.subplots(figsize=(10, 6))

# Crisis zone shading (2007-2012)
ax.axvspan(2007, 2012, alpha=0.15, color=V4_COLORS['MLRED'], label='Crisis Zone (2008)')

# Post-crisis acceleration zone (2012-2024)
ax.axvspan(2012, 2024, alpha=0.07, color=V4_COLORS['MLGREEN'], label='Post-Crisis Acceleration')

# Main S-curve
ax.plot(x_fine, y_curve, color=V4_COLORS['MLTEAL'], linewidth=2.5, zorder=3)

# Plot milestones
for yr, label, yval, yoff in milestones:
    color = V4_COLORS['MLRED'] if yr == 2008 else V4_COLORS['MLTEAL']
    ms = 10 if yr == 2008 else 7
    ax.scatter(yr, yval, color=color, s=ms**2, zorder=5)
    # Stem line
    ax.plot([yr, yr], [yval, yval + yoff * 0.6], color='#AAAAAA', linewidth=0.8, zorder=2)
    fontsize = 7.5
    weight = 'bold' if yr == 2008 else 'normal'
    fc = V4_COLORS['MLRED'] if yr == 2008 else '#333333'
    ax.text(yr, yval + yoff, label, fontsize=fontsize, ha='center', va='center',
            color=fc, fontweight=weight,
            bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='none', alpha=0.8))

apply_v4_style(ax, title='Evolution of Financial Technology: 1950s\u20132020s',
               xlabel='Year', ylabel='Illustrative Adoption / Impact')

ax.set_xlim(1945, 2026)
ax.set_ylim(-0.05, 1.15)
ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
ax.set_yticklabels(['0', 'Low', 'Medium', 'High', 'Very High'])
ax.set_xticks([1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020])

legend_patches = [
    mpatches.Patch(color=V4_COLORS['MLTEAL'], label='Fintech S-Curve'),
    mpatches.Patch(color=V4_COLORS['MLRED'], alpha=0.4, label='2008 Crisis Zone'),
    mpatches.Patch(color=V4_COLORS['MLGREEN'], alpha=0.3, label='Post-Crisis Acceleration'),
]
ax.legend(handles=legend_patches, loc='upper left', fontsize=8, framealpha=0.9)

ax.text(0.99, 0.02, 'Illustrative -- conceptual timeline', transform=ax.transAxes,
        fontsize=7, color='#888888', ha='right', va='bottom', style='italic')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
