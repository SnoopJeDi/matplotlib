from matplotlib.matlab import *
plot([1,2,3])
xlabel('time')
ylabel('volts')
title('A line')
savefig('text_simple.png', size=(400,350))
show()
