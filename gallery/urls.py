from django.urls import path
from . import views
#from django.conf import settings
from django.conf.urls import url

urlpatterns=[
    url('^$', views.home, name = 'home'),
    # url(r'^search/', views.search_results, name='search_results')
]

