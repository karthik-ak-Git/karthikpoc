# filepath: d:\projects\git\karthikpoc\adss\urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Map root URL to home view
    path('upload/', views.upload_image, name='upload'),
    path('processing/<int:pk>/', views.processing_view, name='processing'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
]