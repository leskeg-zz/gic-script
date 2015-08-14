'''Script to get information from Exchange Service SOAP WSDL'''
from suds.client import Client
from datetime import datetime
from ipdb import set_trace
import sys

answer = client.service.GetInformation(datetime.now() - timedelta(minutes=60),datetime.now())
filename=time.strftime("%Y%m%d")
text_file=open(filename + ".xls", "a")

for element in answer.values:
	chargePoints[element.address] = element.valueWh
	print(element.idChargePoint + '\t' + element.city + '\t' + element.address + '\t' + element.rechargeType + '\t' + element.startDateTime.strftime("%Y-%m-%d %H:%M:%S") + '\t' + element.endDateTime.strftime("%Y-%m-%d %H:%M:%S") + '\t' + element.rechargeDateTime.strftime("%Y-%m-%d %H:%M:%S") + element.valueWh )
	text_file.write(element.idChargePoint + '\t' + element.city + '\t' + element.address + '\t' + element.rechargeType + '\t' + element.startDateTime.strftime("%Y-%m-%d %H:%M:%S") + '\t' + element.endDateTime.strftime("%Y-%m-%d %H:%M:%S") + '\t' + element.rechargeDateTime.strftime("%Y-%m-%d %H:%M:%S") + '\t' + element.valueWh + "\n" )

text_file.close()