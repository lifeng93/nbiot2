"""subscribe URL Configuration"""

from django.conf.urls import url
from . import views

urlpatterns =[
  url(r'^datachanged/$', views.datachanged, name='datachanged'),
	url(r'^detail/$', views.detail, name='detail'),
]
app_name = 'subscribe'
