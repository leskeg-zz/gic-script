'''Script to get information from Exchange Service SOAP WSDL'''
from suds.client import Client
from datetime import datetime, timedelta
from ipdb import set_trace
import sys

url = 'http://ocpp.itcl.es/REE/ExchangeInformation.svc?wsdl'
client = Client(url)
answer = client.service.GetInformation(datetime.now() - timedelta(days=1),datetime.now())
# answer = client.service.GetInformation(datetime(2015,8,19,5,30),datetime(2015,8,19,6,0))
if answer:
	print(answer)