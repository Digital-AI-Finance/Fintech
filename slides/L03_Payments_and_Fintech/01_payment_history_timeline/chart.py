"""
Figure 01: Payment History Timeline
Annotated horizontal timeline from barter (3000 BCE) through coinage, paper money,
checks, wire transfers, credit cards, digital wallets, and CBDCs.
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
    'title': 'Payment History Timeline',
    'type': 'time_series',
    'section': 'History of Payments',
    'lecture_number': 3,
}

np.random.seed(42)

milestones = [
    (-3000, 'Barter\nSystems'),
    (-600,  'Coinage\n(Lydia)'),
    (700,   'Paper Money\n(China)'),
    (1659,  'Checks\n(England)'),
    (1872,  'Wire\nTransfers'),
    (1950,  'Credit Cards\n(Diners Club)'),
    (1994,  'Online\nPayments'),
    (2007,  'Mobile\nWallets'),
    (2020,  'CBDCs\n(Pilots)'),
]

colors = [
    V4_COLORS['MLBROWN'], V4_COLORS['MLORANGE'], V4_COLORS['MLYELLOW'],
    V4_COLORS['MLBLUE'], V4_COLORS['MLTEAL'], V4_COLORS['MLPURPLE'],
    V4_COLORS['MLRED'], V4_COLORS['MLGREEN'], V4_COLORS['MLCYAN'],
]

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.set_xlim(-3500, 2200)
ax.set_ylim(-2.5, 3.0)
ax.axis('off')
fig.patch.set_facecolor('white')

# Main timeline arrow
ax.annotate('', xy=(2150, 0), xytext=(-3400, 0),
            arrowprops=dict(arrowstyle='->', color='#AAAAAA', lw=2.5))

# Plot milestones
for i, (year, label) in enumerate(milestones):
    color = colors[i]
    # Alternate above/below
    direction = 1 if i % 2 == 0 else -1
    y_text = 1.6 * direction
    y_dot = 0

    # Dot on timeline
    ax.plot(year, y_dot, 'o', color=color, markersize=10, zorder=5)

    # Vertical connector
    ax.plot([year, year], [y_dot + 0.15 * direction, y_text - 0.35 * direction],
            color=color, linewidth=1.5, linestyle='--', alpha=0.6)

    # Label box
    bbox_props = dict(boxstyle='round,pad=0.3', facecolor=color, alpha=0.15,
                      edgecolor=color, linewidth=1.5)
    ax.text(year, y_text, label, ha='center', va='center',
            fontsize=7.5, fontweight='bold', color=color, bbox=bbox_props)

    # Year label
    y_year = y_text + 0.55 * direction
    year_str = f'{abs(year)} BCE' if year < 0 else str(year)
    ax.text(year, y_year, year_str, ha='center', va='center',
            fontsize=6.5, color='#555555', fontstyle='italic')

ax.set_title('The Evolution of Payments: From Barter to CBDCs',
             fontsize=14, fontweight='bold', pad=15, color='#333333')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
