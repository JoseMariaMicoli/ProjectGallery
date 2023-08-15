from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .models import *
from .forms import ContactForm

# Create your views here.
def home(request):
    categories = Category.objects.all()
    
    context = {}
    context['categories'] = categories
    
    return render(request, 'main/index.html', context)
    
def categoryPage(request, slug):
    category = Category.objects.get(slug=slug)
    images = Image.objects.filter(category=category).order_by('-date_created')[:6]
    for x in images:
        x.shortDescription = x.description[:130]
        
    context = {}
    context['images'] = images
    context['category'] = category
        
    return render(request, 'main/category.html', context)
  
def imageDetailPage(request, slug1, slug2):
    category = Category.objects.get(slug=slug1)
    image = Image.objects.get(slug=slug2)
    
    context = {}
    context['category'] = category
    context['image'] = image
    
    return render(request, 'main/image.html', context)
    
def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            phone = form.cleaned_data["phone"]
            subject = form.cleaned_data["subject"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
        try:
            send_mail(subject, message, email, ["cr4sh.dump@gmail.com"])
        except BadHeaderError:
            return HttpResponse("Error: Invalid header found!")
        return redirect('success')
    return render(request, "main/contact.html", {"form": form})
    
def successView(request):
    return HttpResponse("Success! Thank you for your message. We will respond as soon as possible.")