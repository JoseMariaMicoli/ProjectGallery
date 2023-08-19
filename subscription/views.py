from django.shortcuts import render
from .models import *
from .forms import SubscriptionForm

# Create your views here.
def subscriptionView(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            birth_date = form.cleaned_data["birth_date"]
            #age = form.cleaned_data["age"]
            phone = form.cleaned_data["phone"]
            email = form.cleaned_data["email"]
            dni_number = form.cleaned_data["dni_number"]
            gender = form.cleaned_data["gender"]
            form.save()
    else:
        form = SubscriptionForm()
    
    return render(request, "subscriptions/subscriptions.html", {"form": form})