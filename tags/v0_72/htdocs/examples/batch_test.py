import matplotlib
matplotlib.use('GTK')
from matplotlib.matlab import *
from matplotlib.backends.backend_gtk import ShowOn
ShowOn().set(1)  # turning on interactive mode

t = arange(0.0, 3.0, 0.01)
for i in range(1,10):
    figure(1)
    s = sin(2*pi*i*t)
    plot(t,s)
    #savefig('plot%02d' % i)
    close(1)

