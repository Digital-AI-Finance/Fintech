import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import numpy as np
from pathlib import Path

# Fintech course V4 colors
V4_COLORS = {
    'MLPURPLE': '#9467BD',
    'MLBLUE': '#1F77B4',
    'MLRED': '#D62728',
    'MLORANGE': '#FF7F0E',
    'MLGREEN': '#2CA02C',
    'MLGRAY': '#7F7F7F',
    'MLTEAL': '#0D7377',
    'MLCYAN': '#14BDEB',
    'MLYELLOW': '#BCBD22',
    'MLPINK': '#E377C2',
    'MLBROWN': '#8C564B',
}

# Ordered color cycle for charts
COLOR_CYCLE = [V4_COLORS['MLTEAL'], V4_COLORS['MLORANGE'], V4_COLORS['MLPURPLE'],
               V4_COLORS['MLRED'], V4_COLORS['MLBLUE'], V4_COLORS['MLGREEN'],
               V4_COLORS['MLCYAN'], V4_COLORS['MLYELLOW'], V4_COLORS['MLPINK']]

def apply_v4_style(ax, title='', xlabel='', ylabel=''):
    """Apply consistent V4 styling to a matplotlib axes."""
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
    """Save chart as PDF with tight layout."""
    fig.tight_layout()
    fig.savefig(filename, format='pdf', bbox_inches='tight', dpi=dpi, facecolor='white')
    plt.close(fig)
    print(f'Saved: {filename}')
