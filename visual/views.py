from django.shortcuts import render
from django.http import JsonResponse
from subscribe.models import Temperature

# Create your views here.
def visual(request):
	return render(request, 'visual/example.html')

def return_json(request):
	newdatas = Temperature.objects.filter(deviceId='51c653fc-f1db-4ad5-bcb9-1bf89d9a5a77')\
	.values('temperature', 'eventTime').order_by('-eventTime')[0:10:-1]
	return JsonResponse({'data':newdatas})
	
