from django.urls import path
from . import views
#from django.conf import settings
from django.conf.urls import url

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
]
