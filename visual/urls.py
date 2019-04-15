''' visual URL Configuration'''

from django.conf.urls import url
from . import views

urlpatterns =[
	url(r'^example/$', views.visual, name='example'),
	url(r'^return_json/$', views.return_json, name='return_json'),
]
app_name = 'visual'  