from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # Import the User model
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.
def index(request):
    # return HttpResponse("Hello world")
    return render(request, 'index.html')
def detail(request,post_id):
    return HttpResponse(f"You're looking at detail{post_id}")

def old_url_redirect(request):
    # return redirect("new_url")
    return redirect(reverse("app:new_url"))

def new_url_view(request):
    return HttpResponse("This is the new url")
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                print("user name exists")
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                print("email exists")
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Account created successfully')
                login(request, user)
                return redirect('app:login')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'register.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('app:index')  # Redirect to a home page or other after successful login
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'login.html')
