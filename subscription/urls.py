from django.urls import path
from . import views

urlpatterns = [
    path('subscription/', views.subscriptionView, name='subscription'),
]