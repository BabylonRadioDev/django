from django import forms
from . import models

class UploadFileForm(forms.Form):
    #name = forms.CharField(max_length = 100)
    #docfile = forms.FileField(label = 'Select a file')
    class Meta:
        model = models.uploadcv