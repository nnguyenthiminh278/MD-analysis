import sys
import numpy as np

data=[]
for line in open('total.xvg'):
        li=line.strip()
        if not li.startswith(("#","@")) and li != "":
            data.append(float(li.split()[1]))
print('Average')
print(sum(data)/len(data))
