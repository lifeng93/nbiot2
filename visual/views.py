from django.shortcuts import render
from django.http import JsonResponse
from subscribe.models import Temperature

# Create your views here.
def visual(request):
	return render(request, 'visual/example.html')

def return_json(request):
	newdatas = Temperature.objects.filter(deviceId='5d76557d-a4dd-42ab-822c-a7e6a5b4bd7a')\
	.values('temperature', 'eventTime').order_by('-eventTime')[0:10:-1]
	return JsonResponse({'data':newdatas})
	