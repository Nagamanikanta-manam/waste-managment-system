from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # Import the User model
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import WasteCollectionRequest, Collector

# Create your views here.

def detail(request,post_id):
    return HttpResponse(f"You're looking at detail{post_id}")

@login_required
def index(request):
    return render(request, 'index.html')



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
            print("loged")
            return redirect('app:log')  # Redirect to a home page or other after successful login
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'login.html')
def home_view(request):
    return render(request, 'home.html')
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Home page view (After login)
@login_required
def home_view_l(request):
    return render(request, 'index2.html')

# Waste collection booking view
@login_required
def book_collection_view(request):
    if request.method == 'POST':
        # Retrieve form data from the POST request
        collection_date = request.POST.get('collection_date')
        collection_time = request.POST.get('collection_time')
        address = request.POST.get('address')
        
        # Get the logged-in user
        user = request.user
        
        # You might have a method to select a collector or pick one dynamically
        # For simplicity, assuming the first available collector is picked
        # Replace with your own logic

        # Validate input data (simple validation can be added here)
        if not collection_date or not collection_time or not address:
            return HttpResponse("Please fill all the fields.", status=400)

        # Create and save the new waste collection request
        waste_collection_request = WasteCollectionRequest(
            user=user,
            collection_date=collection_date,
            collection_time=collection_time,
            address=address,
        )
        waste_collection_request.save()

        # Redirect to a success page or show a success message
        return HttpResponse("Waste Collection booked successfully!")
    
    return render(request, 'book_collection.html')
# Waste management statistics view
@login_required
def statistics_view(request):
    # Fetch all waste collection requests placed by the logged-in user
    user_requests = WasteCollectionRequest.objects.filter(user=request.user)

    # Pass the data to the template
    return render(request, 'statistics.html', {'user_requests': user_requests})

# Profile settings view
@login_required
def profile_view(request):
    # Fetch the user's profile data here and allow them to update
    # Example: user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'profile.html')
from django.contrib.auth import logout
def custom_logout(request):
    logout(request)
    return redirect('app:login') 