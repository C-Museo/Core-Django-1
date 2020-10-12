from django.shortcuts import render

def welcome(request):
        title='Welcome to my gallery'
    return render(request, 'gallery/home.html'
        
