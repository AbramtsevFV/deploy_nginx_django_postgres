from django import forms
from .models import Photo
from django.forms import FileInput, Widget, ClearableFileInput


class ImageForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', ]
        error_messages = ''
        widgets = {'image': FileInput(attrs={'class': "d-none", 'onchange': "form.submit()"})
        }