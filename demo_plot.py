import matplotlib.pyplot as plt
import numpy as np
import time

from ipdb import set_trace

# set_trace()

ax = plt.axes(xlim=(0, 24), ylim=(0, 10))
ax.grid(True)
plt.xticks( list(range(0,24)) )

# some X and Y data
lines_quantity = list(range(10))
x = [0]
y = [[0] for _ in lines_quantity]
li = [ax.plot([],[])[0] for _ in lines_quantity]

plt.ion()
plt.show()

# loop to update the data
while True:
	try:
		print(str(x[-1]) + ', ' + str(y[-1]))

		x.append( x[-1]+0.5 )

		for line in lines_quantity:
			y[line].append( np.random.random_sample() * 10 )
			li[ line ].set_xdata(x)
			li[ line ].set_ydata(y[line])

		plt.draw()

		if len(x) > 49:
			x = [0,0.5]
			for line in lines_quantity:
				y[line] = y[line][-2:]

		time.sleep(0.1)
		plt.pause(0.01) 
	except KeyboardInterrupt:
		break