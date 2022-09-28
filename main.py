# Plot all data for the final analysis
# Please name the input files in the same way as in "analysis.sh"

import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pathlib import Path

#=========== Read data ===========
#== Initializing prefix list =====
#=================================

def load_data(data):
    x_arr1 = []
    y_arr1 = []
    for line in open(data):
        li=line.strip()
        if not li.startswith(("#","@")) and li != "":
            x_arr1.append(float(li.split()[0]))
            y_arr1.append(float(li.split()[1]))
    return x_arr1, y_arr1

#=========== Plot data ===========
#== set the x-axis to be in ns ===
#=================================
def plot_data(x_arr1, y_arr1, xlabel, ylabel, color):
    #ax = plt.figure(figsize=(5, 3))
    lns1 = plt.plot(x_arr1, y_arr1, color=color)                
    ax = plt.gca()
    if np.max(x_arr1) > 1e3:
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x/1000)))
    ax.set_xlabel(xlabel, fontsize=20)
    ax.set_ylabel(ylabel, fontsize=20)
    ax.tick_params(
            axis='x',          # changes apply to the x-axis
            labelsize=20
        )
    ax.tick_params(
            axis='y',          # changes apply to the x-axis
            labelsize=20
        )
    plt.tight_layout()
    #ax.text(0, 1000, 'set 1',size=16, ha='center', va='center')
    



path = Path('input')
output = Path('output')
count = 0

#============= Plot data ================
#== set the label for different files ===
#========================================
for file in sorted(path.glob('*.xvg')):
    x, y = load_data(file)
    y = np.array(y)
    name = output / (file.stem + '.pdf')
    if 'INH' in file.name: # rmsd of INH and pocket
        x_label, y_label = 'Time (ns)', 'rmsd'
        count = count + 1
        plot_data(x, y, x_label, y_label, color='red' if count % 2 else 'black')
        plt.ylim((0, 0.25)) 

    elif 'RMSD' in file.name: #rmsd of pocket and protein
        x_label, y_label = 'Time (ns)', 'rmsd'
        count = count + 1
        plot_data(x, y, x_label, y_label, color='red' if count % 2 else 'black')
               
    
    elif 'angaver' in file.name:
        x_label, y_label = 'Time (ns)', '${\phi}$ ($^\circ$)'
        count = count + 1
        y [y < -90] += 360
        #print(y)
        plot_data(x, y, x_label, y_label, color='red' if count % 2 else 'black')
        plt.ylim((-100, 270))

    elif 'angdist' in file.name:
        x_label, y_label = '${\phi}$ ($^\circ$)', 'Probability'
        count = count + 1
        plot_data(x, y, x_label, y_label, color='red' if count % 2 else 'black')

    else:
        # if 'angdist' in file.name:
        #     x_label, y_label = '${\phi}$ ($^\circ$)', 'Probability'
        # elif 'angaver' in file.name:
        #     x_label, y_label = 'Time (ns)', '${\phi}1$ ($^\circ$)'        
        if 'hbnum' in file.name:
            x_label, y_label = 'Time (ns)', 'Number'
            plt.ylim((0, 6))
        elif 'profile' in file.name:
            x_label, y_label = 'Distance (nm)', 'Free Energy (kJ/mol)'
        else:
            x_label, y_label = 'Time (ns)', 'Energy (kJ/mol)'
            import statistics
            print(statistics.mean(y)) 
            plt.ylim((-450, 150))
        plot_data(x, y, x_label, y_label, color='red')
    
    if count % 2 == 0:
        count = 0
        plt.savefig(name, format='pdf')
        plt.close()
        