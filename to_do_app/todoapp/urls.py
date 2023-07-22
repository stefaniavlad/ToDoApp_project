from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_before_login, name='home_before_login'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<id>', views.delete, name='delete'),
    path('cumpara/<id>', views.change_status, name='change_status'),
    path('register', views.register),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logut'),
]
