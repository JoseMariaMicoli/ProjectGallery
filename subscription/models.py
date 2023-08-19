from django.db import models
from django.template.defaultfilters import slugify
from django_resized import ResizedImageField
from django.utils import timezone
from uuid import uuid4
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver
from main.models import Category, Gender
import datetime

# Create your models here.
class Account(models.Model):
    #Main variables
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    birth_date = models.DateField()
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=320)
    approved = models.BooleanField(default=False)
    dni_number = models.CharField(max_length=8)
    dni_front =ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_dni_front.jpg', upload_to='dni')
    dni_back = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_dni_back.jpg', upload_to='dni')
    dni_selfie = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_dni_selfie.jpg', upload_to='dni')
    
    #Related Field
    category = models.OneToOneField(Category, on_delete=models.CASCADE, null=True)
    gender = models.OneToOneField(Gender, on_delete=models.CASCADE, null=True)
    
    #Utility variables
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=500)
    date_created = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return '{} {}'.format(self.dni_number, self.uniqueId)
        
    def get_absolute_url(self):
        return reverse('account-detail', kwargs={'slug': self.slug})
        
    def get_age(self, instance):
        age = datetime.date.today()-self.birth_date
        return int((age).days/365.25)
        
@receiver(pre_save, sender=Account)
def autoPopulateFields(sender, instance, *args, **kwargs):
    if instance.date_created is None:
        instance.date_created = timezone.localtime(timezone.now())
    if instance.uniqueId is None:
        instance.uniqueId = str(uuid4()).split('-')[4]
        instance.slug = slugify('{} {}'.format(instance.dni_number, instance.uniqueId))
            
        instance.slug = slugify('{} {}'.format(instance.dni_number, instance.uniqueId))
        instance.last_updated = timezone.localtime(timezone.now())
        instance.age = instance.get_age(instance)