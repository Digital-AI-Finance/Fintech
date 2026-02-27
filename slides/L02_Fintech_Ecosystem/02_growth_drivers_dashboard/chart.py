"""
Figure 02: Growth Drivers Dashboard
2x2 multi-panel showing VC funding, tech costs, smartphone penetration, digital banking preference.
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
    'title': 'Growth Drivers Dashboard',
    'type': 'multi_panel',
    'section': 'Drivers of Fintech Growth',
    'lecture_number': 2,
}

np.random.seed(42)

fig, axes = plt.subplots(2, 2, figsize=(10, 6))
fig.patch.set_facecolor('white')
fig.suptitle('Fintech Growth Drivers Dashboard', fontsize=14, fontweight='bold',
             color='#333333', y=1.02)

# Top-left: Venture Capital bars
ax = axes[0, 0]
years = list(range(2010, 2024))
vc_data = [2.1, 3.2, 4.0, 5.5, 12.2, 22.3, 18.5, 16.8, 39.6, 34.5, 44.0, 131.5, 75.2, 51.3]
colors_vc = [V4_COLORS['MLTEAL'] if v < 50 else V4_COLORS['MLORANGE'] for v in vc_data]
ax.bar(years, vc_data, color=colors_vc, edgecolor='white', linewidth=0.5)
apply_v4_style(ax, title='Venture Capital ($B)', ylabel='$B')
ax.set_xticks(years[::2])
ax.tick_params(axis='x', rotation=45)

# Top-right: Technology cost declining curve
ax = axes[0, 1]
t_years = np.arange(2005, 2024)
cost_index = 100 * np.exp(-0.15 * (t_years - 2005))
ax.plot(t_years, cost_index, color=V4_COLORS['MLPURPLE'], linewidth=2.5, marker='o', markersize=4)
ax.fill_between(t_years, cost_index, alpha=0.15, color=V4_COLORS['MLPURPLE'])
apply_v4_style(ax, title='Technology Cost Index', ylabel='Index (2005=100)')
ax.set_xticks(t_years[::3])

# Bottom-left: Smartphone penetration S-curve
ax = axes[1, 0]
s_years = np.arange(2007, 2024)
x_norm = (s_years - 2015) / 2.5
penetration = 10 + 70 / (1 + np.exp(-x_norm))
ax.plot(s_years, penetration, color=V4_COLORS['MLGREEN'], linewidth=2.5, marker='s', markersize=4)
ax.fill_between(s_years, penetration, alpha=0.15, color=V4_COLORS['MLGREEN'])
ax.axhline(y=50, color='#CCCCCC', linestyle='--', linewidth=1)
ax.text(2008, 52, '50% threshold', fontsize=7, color='#999999')
apply_v4_style(ax, title='Smartphone Penetration (%)', ylabel='%')
ax.set_ylim(0, 100)
ax.set_xticks(s_years[::3])

# Bottom-right: Digital banking preference by generation
ax = axes[1, 1]
generations = ['Gen Z', 'Millennial', 'Gen X', 'Boomer']
digital = [89, 78, 55, 32]
branch = [11, 22, 45, 68]
x_pos = np.arange(len(generations))
w = 0.35
ax.bar(x_pos - w / 2, digital, w, label='Digital', color=V4_COLORS['MLTEAL'], edgecolor='white')
ax.bar(x_pos + w / 2, branch, w, label='Branch', color=V4_COLORS['MLORANGE'], edgecolor='white')
apply_v4_style(ax, title='Digital vs Branch Preference (%)', ylabel='%')
ax.set_xticks(x_pos)
ax.set_xticklabels(generations, fontsize=8)
ax.legend(fontsize=8, frameon=False)

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
