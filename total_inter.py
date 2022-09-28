#============= Total interaction energy ===============
#==== Extract the total interaction energy (LJ+Col) ===
#=============== module load anaconda =================
#==== python3 total_inter.py LJ-SR.xvg Coul-SR.xvg ===
#======================================================

import sys
import numpy as np

#Read data
# initializing prefix list
sys.stdout = open("total.xvg", "w")
file1 = sys.argv[1]  # LJ
file2 = sys.argv[2]  # Coul

def get_data(data1,data2):
    tot = []
    #get datda 1
    x_arr1 = []
    y_arr1 = []
    for line in open(data1):
        li=line.strip()
        if not li.startswith(("#","@")) and li != "":
            x_arr1.append(float(li.split()[0]))
            y_arr1.append(float(li.split()[1]))

    #get datda 2
    x_arr2 = []
    y_arr2 = []
    
    for line in open(data2):
        li=line.strip()
        if not li.startswith(("#","@")) and li != "":
            x_arr2.append(float(li.split()[0]))
            y_arr2.append(float(li.split()[1]))
    
    tot = np.add(y_arr1, y_arr2)
    for i in range(len(x_arr1)):
        #print("%3i\t%3i" %(x_arr1[i],tot[i]))
        print(x_arr1[i],tot[i])
    
get_data(file1,file2)

#sys.stdout.close()




data=[]
for line in open('total.xvg'):
        li=line.strip()
        if not li.startswith(("#","@")) and li != "":
            data.append(float(li.split()[0]))
print('Average')
print(sum(data)/len(data))
# average = sum(second[0] for first, second in fileArr) // len(fileArr)
# print(average)