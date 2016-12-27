from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'stop/add/$', views.BusStopCreate.as_view(), name='stop-add'),
]
