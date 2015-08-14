import matplotlib.pyplot as plt
import numpy as np
import time

from ipdb import set_trace

# set_trace()

ax = plt.axes(xlim=(0, 24), ylim=(0, 10))
ax.grid(True)
plt.xticks( list(range(0,24)) )
# some X and Y data
x = [0]
y = [np.random.random_sample() * 10]

# y1 = np.random.random_sample(48,) * 10

li, = ax.plot(x, y)
# li1, = ax.plot(x, y1)
# draw and show it
# fig.canvas.draw()
plt.ion()
plt.show()

# loop to update the data
while True:
	try:
		print(str(x[-1]) + ', ' + str(y[-1]))
		# y[:-1] = y[1:]
		# y[-1:] = np.random.random_sample() * 10
		x.append( x[-1]+0.5 )
		y.append( np.random.random_sample() * 10 )
		# y1[:-1] = y1[1:]
		# y1[-1:] = np.random.random_sample() * 10
		# set the new data
		li.set_xdata(x)
		li.set_ydata(y)
		# li1.set_ydata(y1)
		plt.draw()

		if len(x) > 49:
			x = [0,0.5]
			y = y[-2:]
			print(str(x[-2]) + ', ' + str(y[-2]))

		time.sleep(0.1)
		plt.pause(0.01) 
	except KeyboardInterrupt:
		break