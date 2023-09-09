from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'meeting/register.html')

def login(request):
    return render(request, 'meeting/login.html')