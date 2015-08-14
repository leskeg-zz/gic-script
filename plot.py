# -*- coding: utf-8 -*-
'''Script to get information from Exchange Service SOAP WSDL'''

from suds.client import Client
from datetime import datetime, timedelta
from ipdb import set_trace
import sys
import schedule
import time

import matplotlib.pyplot as plt
import numpy as np


url = 'http://ocpp.itcl.es/REE/ExchangeInformation.svc?wsdl'
client = Client(url)

chargePoints = {
	'Calle Cardenal Marcelo Spínola, 10': [0],
	'Calle Santa Engracia, 115': [0],
	'Plaza de la Lealtad, 3': [0],
	'Paseo de la Castellana, 259': [0],
	'Ronda de Valencia, 1': [0],
	'Calle Génova, 24': [0],
	'Calle Manuel Silvela, 16': [0],
	'Calle Cerro de la Plata, 4': [0],
	'Calle Goya, 36': [0],
	'Paseo de la Castellana, 33': [0],
}

ax = plt.axes(xlim=(0, 24), ylim=(-0.1, 10000))
ax.grid(True)
plt.xticks( list(range(0,24)) )

time_now = datetime.now()
# minute_plot = time_now.minute * 10/600
# if minute
time_axis = [ time_now.hour + time_now.minute * 10/600 ]

li = [ax.plot([],[])[0] for _ in chargePoints]

plt.ion()
plt.show()

def job():
	global time_axis
	answer = client.service.GetInformation(datetime.now() - timedelta(minutes=1),datetime.now())
	# answer = type('reply', (object,), {'availableData':False})()
	if answer.availableData:
		print(answer)
		fetchedPoints = { str(element.address):int(element.valueWh) for element in answer.values }
	else:
		fetchedPoints = []

	time_axis.append( time_axis[-1] + 0.5 * 1/60 )
	line_counter = 0

	for chargePoint in chargePoints:
		if chargePoint in fetchedPoints:
			chargePoints[chargePoint].append( fetchedPoints[chargePoint] )
		else:
			chargePoints[chargePoint].append( chargePoints[chargePoint][-1] ) # np.random.random_sample() * 10000

		li[ line_counter ].set_xdata(time_axis)
		li[ line_counter ].set_ydata(chargePoints[chargePoint])
		line_counter+=1

		if time_axis[-2] > 24 - 0.5 * 1/60:
			chargePoints[chargePoint] = chargePoints[chargePoint][-2:]

	if time_axis[-2] > 24 - 0.5 * 1/60:
		time_axis = [ time_axis[-2] - 24 , time_axis[-2] - 24 - 0.5 * 1/60 ]

	plt.draw()
	plt.pause(0.01)

job()
schedule.every(30).seconds.do(job)

while True:
	schedule.run_pending()