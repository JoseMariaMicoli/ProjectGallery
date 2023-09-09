from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def registerView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'meeting/login.html', {'success': "Registration successful. Please login."})
        else:
            error_message = form.errors.as_text()
            return render(request, 'register.html', {'Error': error_message})
        
    return render(request, 'meeting/register.html')

def loginView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/dashboard")
        else:
            return render(request, 'meeting/login.html', {'error': "Invalid credentials. Please try again."})

    return render(request, 'meeting/login.html')

@login_required
def dashboardView(request):
    return render(request, 'meeting/dashboard.html')