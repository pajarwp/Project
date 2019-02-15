from django.urls import path
from . import views

urlpatterns = [
    path('', views.isi_home, name='home'),
    path('about', views.isi_about, name='about'),
    path('fun', views.isi_fun, name='fun'),
]