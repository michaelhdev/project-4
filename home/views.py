from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def get_homepage(request):
    """Return the index.html file"""
    return render(request, "index.html")