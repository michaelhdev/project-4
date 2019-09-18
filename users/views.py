from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from users.forms import UserLoginForm

# Create your views here.

def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out!")
    return redirect(reverse('index'))
    
def login(request):
    """Return login page"""
    login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})
