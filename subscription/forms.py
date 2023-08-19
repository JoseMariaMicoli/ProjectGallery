from django import forms
from django.core.validators import EmailValidator
from django.forms import TextInput, EmailInput
from main.models import Gender
from .models import Account
import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

class SubscriptionForm(forms.ModelForm):
    
    class Meta:
        model = Account
        
        fields = ["first_name", "last_name", "birth_date", "phone", "email", "dni_number", "gender"]
    
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'style': 'width: 300px;', 'class': 'form-control'}), required=True)
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'style': 'width: 300px;', 'class': 'form-control'}), required=True)
    
    this_year = datetime.date.today().year
    year_range = [x for x in range(this_year - 100, this_year + 1)]
    
    birth_date = forms.DateField(label='Birth Date', widget=forms.SelectDateWidget(years=year_range, attrs={'placeholder': 'Birth Date', 'style': 'width: 300px;', 'class': 'form-control'}), required=True)
    #age = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Age', 'style': 'width: 300px;', 'class': 'form-control'}), required=True)
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Phone', 'style': 'width: 300px;', 'class': 'form-control'}), required=True)
    email = forms.CharField(validators=[EmailValidator()], widget=forms.EmailInput(attrs={'placeholder' :'Email', 'style': 'width: 300px;', 'class': 'form-control'}), required=True)
    dni_number = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'placeholder': 'D.N.I.', 'style': 'width: 300px;', 'class': 'form-control'}), required=True)
    gender = forms.ModelChoiceField(queryset=Gender.objects.all(), widget=forms.Select(attrs={'placeholder': 'Gender', 'style': 'width: 300px;', 'class': 'form-control dropdownMenuButtont'}), required=True)