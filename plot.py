from Bio import SeqIO
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd
from mpldatacursor import datacursor
from scipy.signal import find_peaks
record = SeqIO.read("PThio_Burst_0.004_TLD_6_12_19_2019-06-12_C04.fsa",'abi')

from collections import defaultdict

trace = defaultdict(list)

trace['DATA1'] = record.annotations['abif_raw']['DATA1']

indices = find_peaks(trace['DATA1'],threshold=20)[0]


print(indices)
fig, ax = plt.subplots()
data = ax.plot(trace['DATA1'])
datacursor(data)
for i in range(len(indices)):
    ax.plot(indices[i],trace['DATA1'][indices[i]],'r*',markersize=9,picker=5)

def onpick(event):
    thisline = event.artist
    xdata = thisline.get_xdata()
    ydata = thisline.get_ydata()
    ind = event.ind
    points = tuple(zip(xdata[ind], ydata[ind]))
    print('onpick points:', points)

fig.canvas.mpl_connect('pick_event', onpick)

plt.show()
