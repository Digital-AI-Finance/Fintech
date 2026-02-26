"""
Figure 09: Fintech Impact Comparison by Region
Grouped bar chart: 5 regions x 4 categories on 1-10 illustrative scale.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '_shared'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
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
    'title': 'Fintech Adoption by Region (Illustrative)',
    'type': 'comparison_bar',
    'section': 'WHERE',
    'lecture_number': 1,
}

regions = ['North\nAmerica', 'Europe', 'Asia-\nPacific', 'Africa /\nMiddle East', 'Latin\nAmerica']
categories = ['Mobile Payments', 'Digital Lending', 'Neobanks', 'InsurTech']
colors = [V4_COLORS['MLTEAL'], V4_COLORS['MLPURPLE'],
          V4_COLORS['MLORANGE'], V4_COLORS['MLGREEN']]

# Illustrative adoption scores (1-10): rows = regions, cols = categories
# North America: high digital lending/neobanks, medium mobile payments
# Europe: high neobanks (open banking), medium others
# Asia-Pacific: very high mobile payments (Alipay, WeChat), high lending
# Africa/ME: very high mobile payments (M-Pesa), low others
# Latin America: high mobile payments (PIX), growing others
scores = np.array([
    [6.5, 8.0, 7.0, 6.0],  # North America
    [6.0, 7.0, 8.5, 6.5],  # Europe
    [9.5, 8.0, 7.5, 7.0],  # Asia-Pacific
    [8.0, 4.5, 3.5, 4.0],  # Africa/ME
    [7.0, 6.0, 5.5, 5.0],  # Latin America
])

n_regions = len(regions)
n_cats = len(categories)
x = np.arange(n_regions)
group_width = 0.7
bar_width = group_width / n_cats
offsets = np.arange(n_cats) * bar_width - group_width / 2 + bar_width / 2

fig, ax = plt.subplots(figsize=(10, 6))

for c_idx, (cat, color) in enumerate(zip(categories, colors)):
    vals = scores[:, c_idx]
    positions = x + offsets[c_idx]
    bars = ax.bar(positions, vals, width=bar_width * 0.88,
                  color=color, alpha=0.85, label=cat)

apply_v4_style(ax,
               title='Illustrative Fintech Adoption by Region and Category',
               xlabel='Region',
               ylabel='Adoption Score (1\u201310, illustrative)')

ax.set_xticks(x)
ax.set_xticklabels(regions, fontsize=9)
ax.set_ylim(0, 11.5)
ax.set_yticks([0, 2, 4, 6, 8, 10])
ax.axhline(y=5, color='#DDDDDD', linewidth=0.8, linestyle='--', zorder=0)

ax.legend(loc='upper right', fontsize=9, framealpha=0.9, title='Category', title_fontsize=9)

# Annotate leapfrog note
ax.annotate('Leapfrog effect:\nhigh mobile, low\ntraditional banking',
            xy=(3, 8.0), xytext=(3.55, 10.2),
            fontsize=7.5, color=V4_COLORS['MLTEAL'],
            arrowprops=dict(arrowstyle='->', color=V4_COLORS['MLTEAL'], lw=1.2),
            ha='left', va='top')

ax.text(0.5, -0.14, 'Conceptual adoption levels \u2014 illustrative comparison. Not actual survey or market data.',
        transform=ax.transAxes, fontsize=8, color='#888888',
        ha='center', va='center', style='italic')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
