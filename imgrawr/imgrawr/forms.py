from django import forms

class UploadFileForm(forms.Form):
    tags = forms.CharField(max_length=50)
    file = forms.FileField()