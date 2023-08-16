from django.db import models
from django.template.defaultfilters import slugify
from django_resized import ResizedImageField
from django.utils import timezone
from uuid import uuid4
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Gender(models.Model):
    name = models.TextField(null=True, blank=True, max_length=100)
    description = models.TextField(null=True, blank=True)
    
    #Utility variables
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=500)
    date_created = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return '{} {}'.format(self.name, self.uniqueId)
        
    def get_absolute_url(self):
        return reverse('gender-detail', kwargs={'slug', self.slug})

# Create your models here.
class Category(models.Model):
    #main Category variable
    title = models.CharField(null=True, blank=True, max_length=300)
    
    #Related Fields
    gender = models.ForeignKey(Gender, null=True, blank=True, on_delete=models.CASCADE)
    
    #Utility variables
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=500)
    date_created = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)
        
    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})
        
    """def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
            
            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
            self.last_updated = timezone.localtime(timezone.now())
            super(Category, self).save(*args, **kwargs)"""
            
class Image(models.Model):
    description = models.TextField(null=True, blank=True)
    altText = models.TextField(null=True, blank=True)
    hashtag = models.CharField(null=True, blank=True, max_length=300)
    
    #Image Fields
    squareImage = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_square.jpg', upload_to='square')
    landscapeImage = ResizedImageField(size=[2678, 1618], crop=['middle', 'center'], default='default_land.jpg', upload_to='landscape')
    tallImage = ResizedImageField(size=[1618, 2878], crop=['middle', 'center'], default='default_tall.jpg', upload_to='tall')
    
    
    #Related Fields
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)
    
    #Utility variables
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=500)
    date_created = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return '{} {}'.format(self.name, self.uniqueId)
        
    def get_absolute_url(self):
        return reverse('gender-detail', kwargs={'slug', self.slug})
        
    """def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.category.title, self.uniqueId))
            
            self.slug = slugify('{} {}'.format(self.category.title, self.uniqueId))
            self.last_updated = timezone.localtime(timezone.now())
            
            super(Image, self).save(*args, **kwargs)"""

@receiver(pre_save, sender=Category)
def autoPopulateFields(sender, instance, *args, **kwargs):
    if instance.date_created is None:
        instance.date_created = timezone.localtime(timezone.now())
    if instance.uniqueId is None:
        instance.uniqueId = str(uuid4()).split('-')[4]
        instance.slug = slugify('{} {}'.format(instance.title, instance.uniqueId))
            
        instance.slug = slugify('{} {}'.format(instance.title, instance.uniqueId))
        instance.last_updated = timezone.localtime(timezone.now())     
               
@receiver(pre_save, sender=Image)
def autoPopulateFields(sender, instance, *args, **kwargs):
    if instance.date_created is None:
        instance.date_created = timezone.localtime(timezone.now())
    if instance.uniqueId is None:
        instance.uniqueId = str(uuid4()).split('-')[4]
        instance.slug = slugify('{} {}'.format(instance.category.title, instance.uniqueId))
            
        instance.slug = slugify('{} {}'.format(instance.category.title, instance.uniqueId))
        instance.last_updated = timezone.localtime(timezone.now())
        
@receiver(pre_save, sender=Gender)
def autoPopulateFields(sender, instance, *args, **kwargs):
    if instance.date_created is None:
        instance.date_created = timezone.localtime(timezone.now())
    if instance.uniqueId is None:
        instance.uniqueId = str(uuid4()).split('-')[4]
        instance.slug = slugify('{} {}'.format(instance.name, instance.uniqueId))
            
        instance.slug = slugify('{} {}'.format(instance.name, instance.uniqueId))
        instance.last_updated = timezone.localtime(timezone.now())