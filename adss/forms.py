# imageapp/forms.py
from django import forms
from .models import ImageUpload

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = ['original_image', 'action', 'format']
        widgets = {
            'action': forms.Select(attrs={
                'id': 'action-select',
                'onchange': "toggleFormatField()"
            }),
            'format': forms.Select(attrs={
                'id': 'format-field',
                'style': 'display: none;'
            }),
        }