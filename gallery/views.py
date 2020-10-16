from django.shortcuts import render
from django.http  import HttpResponse
#from forms import *
from .models import Image

def home(request):
    return render (request, 'home.html')

#def welcome(request):
    #title='Welcome to my gallery'
    #images=Image.objects.all()
    #return render( request, '/home.html' ,{'title': title, 'images': images} )

#def search_results(request):

    #return HttpResponse('html')
