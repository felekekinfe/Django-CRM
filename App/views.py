from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You Logged in')
            return redirect('home')
        else:
            messages.success(request, "Error Try Again")
            return redirect('home')

    return render(request, 'App/templates/home.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'You Logged Out...')
    return redirect('home')
def register_user(request):
    return render(request, 'register.html')