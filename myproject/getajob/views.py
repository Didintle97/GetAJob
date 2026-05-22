from django.shortcuts import render, redirect
from .models import Product, Jobseeker, Vendor, Job
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .forms import SignUpForm
# Create your views here.


def home(request):
    products = Product.objects.all()
    jobseekers = Jobseeker.objects.all()
    vendors = Vendor.objects.all()
    jobs = Job.objects.all()
    return render(request, 'home.html', {'products': products, 
                                          'jobseekers': jobseekers, 
                                           'vendors': vendors,
                                           'jobs': jobs})


def about(request):
    return render(request, 'about.html', {})
 

def login_user(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You've been logged in!"))
            return redirect('home') 
        else: 
            messages.success(request, ("There was an error. You are not logged in!"))
            return redirect('login')
    else:
         return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You are logged out"))
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have registered successfully"))
            return redirect('home')
        else:
            messages.success(request, ("There was a problem registering. Please try again"))
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})
    