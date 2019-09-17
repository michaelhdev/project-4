from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def get_homepage(request):
    
    return render(request, "index.html")