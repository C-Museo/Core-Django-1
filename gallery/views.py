from django.shortcuts import render
from django.http  import HttpResponse

def welcome(request):
    title='Welcome to my gallery'
    return render( request, 'gallery/home.html' ,{'title': title} )

def search_results(request):

    return HttpResponse(html)
