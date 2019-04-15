from django.shortcuts import render
from django.http import HttpResponse
import json
import time
import datetime

from .models import Temperature

# Create your views here.
def datachanged(request):
	if request.method == 'POST':
		body = json.loads(request.body)
		if len(body)>0:
			deviceId = body['deviceId']
			service = body['service']
			serviceId = service['serviceId']
			data = service['data']
			eventTime = service['eventTime']
			eventTime = time.strptime(eventTime, '%Y%m%dT%H%M%SZ')
			eventTime = time.mktime(eventTime)
			eventTime = datetime.datetime.fromtimestamp(eventTime)
			if serviceId == 'Temperature':
				temperature = data['temperature']
				print(temperature)
			temper = Temperature()
			temper.deviceId = deviceId
			temper.temperature = temperature
			temper.eventTime = eventTime
			temper.save()
		else:
			print('no body')
	return HttpResponse(status=200, reason='ok')
