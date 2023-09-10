from django.urls import path
from . import views

urlpatterns = [
    path('meeting/register/', views.registerView, name='register'),
    path('meeting/login/', views.loginView, name='login'),
    path('meeting/dashboard/', views.dashboardView, name='dashboard'),
    path('meeting/meeting/', views.videocall, name='meeting'),
    path('meeting/logout/', views.logoutView, name='logout'),
    path('meeting/join/', views.join_room, name='join_room'),
    path('meeting/', views.index, name='index'),
]
