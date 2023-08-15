from django import forms
from django.core.validators import EmailValidator
from django.forms import TextInput, EmailInput

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    email = forms.CharField(validators=[EmailValidator()], widget=forms.EmailInput(attrs={'placeholder' :'Email', 'style': 'width: 300px;', 'class': 'form-control'}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Phone', 'style': 'width: 300px;', 'class': 'form-control'}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Phone', 'style': 'width: 300px;', 'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Message', 'style': 'width: 300px;', 'class': 'form-control'}), required=True)