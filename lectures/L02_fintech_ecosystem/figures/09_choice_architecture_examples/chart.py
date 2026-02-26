"""
Figure 09: Choice Architecture Examples
2x2 quadrant mapping financial inclusion vs consumer protection.
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
    'title': 'Choice Architecture Examples',
    'type': 'quadrant',
    'section': 'Choice Architecture',
    'lecture_number': 2,
}

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
fig.patch.set_facecolor('white')

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Quadrant fills
# Q1: High Inclusion, High Protection (top-right) - green
ax.fill_between([5, 10], [5, 5], [10, 10], alpha=0.12, color=V4_COLORS['MLGREEN'])
# Q2: High Inclusion, Low Protection (bottom-right) - red
ax.fill_between([5, 10], [0, 0], [5, 5], alpha=0.12, color=V4_COLORS['MLRED'])
# Q3: Low Inclusion, High Protection (top-left) - blue
ax.fill_between([0, 5], [5, 5], [10, 10], alpha=0.12, color=V4_COLORS['MLBLUE'])
# Q4: Low Inclusion, Low Protection (bottom-left) - gray
ax.fill_between([0, 5], [0, 0], [5, 5], alpha=0.12, color=V4_COLORS['MLGRAY'])

# Dividing lines
ax.axhline(y=5, color='#AAAAAA', linewidth=1.5, linestyle='-')
ax.axvline(x=5, color='#AAAAAA', linewidth=1.5, linestyle='-')

# Q1: Regulated Mobile Money (top-right)
ax.text(7.5, 8.0, 'Regulated\nMobile Money', ha='center', va='center',
        fontsize=12, fontweight='bold', color=V4_COLORS['MLGREEN'])
ax.text(7.5, 6.8, 'M-Pesa, UPI, Pix', ha='center', va='center',
        fontsize=9, color='#555555', fontstyle='italic')

# Q2: Unregulated Micro-lending (bottom-right)
ax.text(7.5, 3.0, 'Unregulated\nMicro-lending', ha='center', va='center',
        fontsize=12, fontweight='bold', color=V4_COLORS['MLRED'])
ax.text(7.5, 1.8, 'Predatory apps,\nhigh-interest lenders', ha='center', va='center',
        fontsize=9, color='#555555', fontstyle='italic')

# Q3: Traditional Banking (top-left)
ax.text(2.5, 8.0, 'Traditional\nBanking', ha='center', va='center',
        fontsize=12, fontweight='bold', color=V4_COLORS['MLBLUE'])
ax.text(2.5, 6.8, 'Well-regulated,\nlimited reach', ha='center', va='center',
        fontsize=9, color='#555555', fontstyle='italic')

# Q4: Informal Finance (bottom-left)
ax.text(2.5, 3.0, 'Informal\nFinance', ha='center', va='center',
        fontsize=12, fontweight='bold', color=V4_COLORS['MLGRAY'])
ax.text(2.5, 1.8, 'ROSCAs, loan sharks,\nmattress savings', ha='center', va='center',
        fontsize=9, color='#555555', fontstyle='italic')

# Goal arrow from Q4 to Q1
ax.annotate('', xy=(6.8, 7.0), xytext=(3.2, 3.8),
            arrowprops=dict(arrowstyle='->', color=V4_COLORS['MLTEAL'],
                            lw=3, connectionstyle='arc3,rad=0.2'))
ax.text(4.2, 6.0, 'GOAL', ha='center', va='center',
        fontsize=11, fontweight='bold', color=V4_COLORS['MLTEAL'],
        rotation=35)

# Axis labels
ax.set_xlabel('Financial Inclusion', fontsize=12, fontweight='bold', color='#555555')
ax.set_ylabel('Consumer Protection', fontsize=12, fontweight='bold', color='#555555')
ax.text(0.2, 5, 'Low', fontsize=9, color='#888888', va='center')
ax.text(9.5, 5, 'High', fontsize=9, color='#888888', va='center', ha='right')
ax.text(5, 0.2, 'Low', fontsize=9, color='#888888', ha='center')
ax.text(5, 9.7, 'High', fontsize=9, color='#888888', ha='center')

ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_color('#CCCCCC')
    spine.set_visible(True)

ax.set_title('Choice Architecture: Inclusion vs Protection',
             fontsize=14, fontweight='bold', pad=15, color='#333333')

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
