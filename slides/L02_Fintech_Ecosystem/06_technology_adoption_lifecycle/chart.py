"""
Figure 06: Technology Adoption Lifecycle
Rogers' bell curve with fintech-specific segment labels and "The Chasm" marker.
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
    'title': 'Technology Adoption Lifecycle',
    'type': 'bell_curve',
    'section': 'Adoption Theory',
    'lecture_number': 2,
}

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
fig.patch.set_facecolor('white')

# Gaussian bell curve
x = np.linspace(-3.5, 3.5, 1000)
y = np.exp(-x**2 / 2) / np.sqrt(2 * np.pi)

# Segment boundaries (in std devs from mean)
# Innovators: 2.5% -> left of -2
# Early Adopters: 13.5% -> -2 to -1
# Early Majority: 34% -> -1 to 0
# Late Majority: 34% -> 0 to 1
# Laggards: 16% -> right of 1
bounds = [-3.5, -2.0, -1.0, 0.0, 1.0, 3.5]
colors = [V4_COLORS['MLPURPLE'], V4_COLORS['MLORANGE'], V4_COLORS['MLTEAL'],
          V4_COLORS['MLBLUE'], V4_COLORS['MLGRAY']]
labels = ['Innovators\n(2.5%)', 'Early\nAdopters\n(13.5%)', 'Early\nMajority\n(34%)',
          'Late\nMajority\n(34%)', 'Laggards\n(16%)']
fintech_labels = ['Crypto\nenthusiasts', 'Tech-savvy\nmillennials', 'Mainstream\ndigital banking',
                  'Reluctant\nconverters', 'Cash\nonly']

for i in range(5):
    mask = (x >= bounds[i]) & (x <= bounds[i + 1])
    ax.fill_between(x[mask], y[mask], alpha=0.6, color=colors[i], label=labels[i].replace('\n', ' '))
    # Segment label at center
    cx = (bounds[i] + bounds[i + 1]) / 2
    cy_idx = np.argmin(np.abs(x - cx))
    ax.text(cx, y[cy_idx] + 0.02, labels[i], ha='center', va='bottom',
            fontsize=7.5, fontweight='bold', color='#333333')
    ax.text(cx, -0.035, fintech_labels[i], ha='center', va='top',
            fontsize=7, color=colors[i], fontstyle='italic')

# Plot the curve outline
ax.plot(x, y, color='#333333', linewidth=1.5)

# THE CHASM - between Early Adopters and Early Majority
chasm_x = -1.0
ax.axvline(x=chasm_x, color=V4_COLORS['MLRED'], linestyle='--', linewidth=2, alpha=0.8)
ax.text(chasm_x, 0.32, 'THE\nCHASM', ha='center', va='bottom',
        fontsize=11, fontweight='bold', color=V4_COLORS['MLRED'])

# Arrow: "Most fintechs are HERE"
ax.annotate('Most fintechs\nare HERE',
            xy=(-1.5, 0.18), xytext=(-2.8, 0.35),
            fontsize=9, fontweight='bold', color=V4_COLORS['MLRED'],
            arrowprops=dict(arrowstyle='->', color=V4_COLORS['MLRED'], lw=2),
            ha='center')

ax.set_ylim(-0.07, 0.48)
ax.set_xlim(-3.5, 3.5)
ax.set_xticks([])
ax.set_yticks([])

apply_v4_style(ax, title='Technology Adoption Lifecycle in Fintech',
               xlabel='Market Penetration')
ax.spines['left'].set_visible(False)

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
