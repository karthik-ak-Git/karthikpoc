# imageapp/models.py
from django.db import models
from django.contrib.auth.models import User

class ImageUpload(models.Model):
    ACTION_CHOICES = [
        ('convert', 'Convert Format'),
        ('resize', 'Resize Image'),
        ('grayscale', 'Grayscale Conversion'),
        ('rotate', 'Rotate Image'),
        ('blur', 'Blur Image'),
        ('brighten', 'Brighten Image'),
        ('contrast', 'Adjust Contrast'),
        ('flip', 'Flip Image'),
    ]
    
    FORMAT_CHOICES = [
        ('JPEG', 'JPEG'),
        ('PNG', 'PNG'),
        ('WEBP', 'WEBP'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_image = models.ImageField(upload_to='uploads/')
    processed_image = models.ImageField(upload_to='processed/', blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    format = models.CharField(max_length=5, choices=FORMAT_CHOICES, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.action}"