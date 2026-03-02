"""
Figure 10: RegTech Investment Trends
Dual-axis chart with bar chart for investment volume (billions) and line
for deal count, with annotated regulatory milestones (2015-2025).
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
    'title': 'RegTech Investment Trends',
    'type': 'time_series',
    'section': 'RegTech Solutions',
    'lecture_number': 4,
}

np.random.seed(42)

years = list(range(2015, 2026))
# Illustrative investment volumes ($ billions)
investment = [1.2, 1.8, 2.5, 4.1, 5.2, 6.8, 8.3, 10.5, 12.1, 14.8, 18.2]
# Illustrative deal counts
deals = [85, 110, 145, 195, 230, 260, 310, 355, 390, 420, 480]

fig, ax1 = plt.subplots(1, 1, figsize=(10, 6))
fig.patch.set_facecolor('white')

# Bar chart for investment volume
bars = ax1.bar(years, investment, width=0.6, color=V4_COLORS['MLBLUE'],
               alpha=0.75, edgecolor='white', linewidth=1, label='Investment ($B)')

apply_v4_style(ax1, title='RegTech Investment Trends (2015-2025)',
               xlabel='Year', ylabel='Investment Volume ($B)')
ax1.set_ylim(0, 22)
ax1.yaxis.grid(True, alpha=0.3, linestyle='--')
ax1.set_axisbelow(True)

# Secondary axis for deal count
ax2 = ax1.twinx()
ax2.plot(years, deals, color=V4_COLORS['MLRED'], linewidth=2.5,
         marker='o', markersize=5, label='Deal Count', zorder=5)
ax2.set_ylabel('Number of Deals', fontsize=11, color=V4_COLORS['MLRED'])
ax2.tick_params(axis='y', colors=V4_COLORS['MLRED'], labelsize=9)
ax2.spines['right'].set_color(V4_COLORS['MLRED'])
ax2.spines['top'].set_visible(False)
ax2.set_ylim(0, 550)

# Milestone annotations
milestones = [
    (2018, 'GDPR\nEnforced', 17.5),
    (2019, 'FCA Sandbox\nExpansion', 14.5),
    (2020, 'MiCA\nProposal', 11.5),
    (2023, 'AI Act\nDraft', 19.0),
]

for year, label, y_pos in milestones:
    ax1.annotate(label,
                 xy=(year, investment[year - 2015]),
                 xytext=(year, y_pos),
                 fontsize=7, fontweight='bold', color='#555555',
                 ha='center', va='bottom',
                 arrowprops=dict(arrowstyle='->', color='#999999',
                                 lw=1.2, alpha=0.7),
                 bbox=dict(boxstyle='round,pad=0.2', facecolor='#F5F5F5',
                           edgecolor='#CCCCCC', linewidth=0.8))

# Combined legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left',
           fontsize=9, frameon=True, fancybox=True, framealpha=0.9)

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
