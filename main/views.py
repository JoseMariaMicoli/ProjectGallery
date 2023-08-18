from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    categories = Category.objects.all()
    genders = Gender.objects.all()
    
    context = {}
    context['categories'] = categories
    context['genders'] = genders
    
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
    
def genderView(request, slug):
    gender = Gender.objects.get(slug=slug)
    categories = Category.objects.filter(gender=gender).order_by('-date_created')
        
    context = {}
    context['categories'] = categories
    context['gender'] = gender
    
    return render(request, "main/gender.html", context)