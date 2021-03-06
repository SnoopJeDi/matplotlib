# a bar plot with errorbars
# a bar plot with errorbars
from matplotlib.matlab import *

N = 5
menMeans = (20, 35, 30, 35, 27)
menStd =   (2, 3, 4, 1, 2)

ind = arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars
p1 = bar(ind, menMeans, width, color='r', yerr=menStd)

womenMeans = (25, 32, 34, 20, 25)
womenStd =   (3, 5, 2, 3, 3)
p2 = bar(ind+width, womenMeans, width, color='y', yerr=womenStd)

ylabel('Scores')
title('Scores by group and gender')
set(gca(), 'xticks', ind+width)
set(gca(), 'xticklabels', ('G1', 'G2', 'G3', 'G4', 'G5') )
set(gca(), 'xlim', [-width,len(ind)])
set(gca(), 'yticks', arange(0,41,10))

legend( (p1[0], p2[0]), ('Men', 'Women') )

savefig('barchart_demo_small.png', dpi=60)
savefig('barchart_demo_large.png', dpi=120)


show()
