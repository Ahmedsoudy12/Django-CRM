from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def home(request):
    # Check to see if logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been loggedin!")
            return redirect('home')
        
        else:
            messages.success(request, "There was and error logging in please try again!")
            return redirect('home')
    else:
        return render(request, 'home.html', {})
    


       

def logout_user(request):   # My view can't be named login because it will conflict with logout lib. from django.contrib.auth
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')



def register_user(request):
    return render(request, 'register.html', {})



