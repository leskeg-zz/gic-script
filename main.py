'''Script to get information from Exchange Service SOAP WSDL'''
from suds.client import Client
from datetime import datetime
from ipdb import set_trace
import sys

start_date = sys.argv[1]
end_date = sys.argv[2]
url = 'http://ocpp.itcl.es/REE/ExchangeInformation.svc?wsdl'
client = Client(url)
print(client.service.GetInformation( \
	datetime(int(start_date.split('/')[2]), int(start_date.split('/')[1]), int(start_date.split('/')[0]), int(start_date.split('/')[3]), 0, 0, 0), \
	datetime(int(end_date.split('/')[2]), int(end_date.split('/')[1]), int(end_date.split('/')[0]), int(end_date.split('/')[3]), 0, 0, 0))
)