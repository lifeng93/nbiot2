"""subscribe URL Configuration"""

from django.conf.urls import url
from . import views

urlpatterns =[
  url(r'^datachanged/$', views.datachanged, name='datachanged'),
]
app_name = 'subscribe'