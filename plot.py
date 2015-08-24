# -*- coding: utf-8 -*-
'''Script to get information from Exchange Service SOAP WSDL'''

from suds.client import Client
from datetime import datetime, timedelta
from ipdb import set_trace
from pprint import pprint
import sys
import schedule
import time

import matplotlib.pyplot as plt
import numpy as np

freq = 30 #Freq of refresh in minutes
url = 'http://ocpp.itcl.es/REE/ExchangeInformation.svc?wsdl'
client = Client(url)

chargePoints = {
	'Calle Cardenal Marcelo Spínola, 10': [],
	'Calle Santa Engracia, 115': [],
	'Plaza de la Lealtad, 3': [],
	'Paseo de la Castellana, 259': [],
	'Ronda de Valencia, 1': [],
	'Calle Génova, 24': [],
	'Calle Manuel Silvela, 16': [],
	'Calle Cerro de la Plata, 4': [],
	'Calle Goya, 36': [],
	'Paseo de la Castellana, 33': [],
}

ax = plt.axes(xlim=(0, 24), ylim=(-0.1, 20000))
ax.grid(True)
plt.xticks( list(range(0,24)) )

time_axis = [[] for _ in chargePoints]
values_axis = [[] for _ in chargePoints]
li = [ax.plot([],[])[0] for _ in chargePoints]

plt.ion()
plt.show()

def job():
	global time_axis, values_axis, li, freq
	time_now = datetime.now()
	answer = client.service.GetInformation( time_now - timedelta(minutes=freq), time_now )
	# answer = type('reply', (object,), {'availableData':False})()
	if answer.availableData:
		print(answer)
		for element in answer.values:
			chargePoints[ element.address ].append( [element.rechargeDateTime, element.valueWh] )

	for chargePoint in chargePoints:
		data_size = len(chargePoints[chargePoint])
		if data_size == 0:
			chargePoints[chargePoint] = [(time_now,0)]
			# THIS LOOP IS TO FIX DATA SOURCE TIME BUG +-1 FROM PROVIDER, SHOULD BE REMOVED WHEN PROVIDER FIXS IT
		# else:
			# for data in chargePoints[chargePoint]:
			# 	# set_trace()
			# 	diff_time = time_now - data[0].replace(tzinfo=None)
			# 	if diff_time.total_seconds() > 60*freq: # 2400 seconds = 40 minutes
			# 		data[0] = data[0] + timedelta(hours=1)
			# 	elif diff_time < 0:
			# 		data[0] = data[0] - timedelta(hours=1)

	line_counter = 0

	# Clear plot after 12PM
	diff_time = time_now - datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
	if diff_time.total_seconds() < 60*freq:
		time_axis = [[] for _ in chargePoints]
		values_axis = [[] for _ in chargePoints]

	for chargePoint in chargePoints:
		for sample in chargePoints[chargePoint]:
			time_axis[line_counter].append(sample[0].hour + sample[0].minute * 1/60)
			values_axis[line_counter].append(sample[1])
		chargePoints[chargePoint] = [] 
		li[ line_counter ].set_xdata(time_axis[line_counter])
		li[ line_counter ].set_ydata(values_axis[line_counter])
		line_counter+=1

	pprint(values_axis)
	pprint(time_axis)

job()
schedule.every(freq).minutes.do(job)

while True:
	schedule.run_pending()
	plt.draw()
	plt.pause(0.01)