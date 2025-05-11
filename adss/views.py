from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import ImageUploadForm
from .models import ImageUpload
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout  # Import the logout function


def register(request):
    """Handle user registration"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please check the form.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})  # Removed imageapp/


#@login_required # temporarily remove login required
def home(request):
    """Display the home dashboard"""
    print("Home view is being called!")  # Add this line
    recent_uploads = ImageUpload.objects.filter(user=request.user).order_by('-upload_date')[:3]
    print(f"Attempting to render: index.html")
    return render(request, 'index.html', {'recent_uploads': recent_uploads})
# filepath: d:\projects\git\karthikpoc\adss\views.py

@login_required
def upload_image(request):
    """Handle image upload and processing"""
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                # handle_image_processing(instance)
                messages.success(request, 'Image uploaded successfully! Processing...')
                return redirect('converter', pk=instance.pk)
            except Exception as e:
                messages.error(request, f'Error processing image: {str(e)}')
                return redirect('converter')
        else:
            messages.error(request, 'Invalid form submission')
    else:
        form = ImageUploadForm()

    return render(request, 'converter.html', {'form': form}) # Make sure this line points to the correct template

@login_required
def processing_view(request, pk):
    """Display processing results"""
    try:
        image = ImageUpload.objects.get(pk=pk, user=request.user)
        context = {
            'image': image,
            'actions': {
                'convert': 'Format Conversion',
                'resize': 'Resizing',
                'grayscale': 'Grayscale Conversion',
                'rotate': 'Rotation'
            }
        }
        return render(request, 'converter.html', context)
    except ImageUpload.DoesNotExist:
        messages.error(request, 'Image not found')
        return redirect('home')


def logout_view(request):
    """Handle user logout"""
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('login')  # Redirect to the login page