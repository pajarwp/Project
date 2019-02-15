from django.urls import path

from . import views

urlpatterns = [
    path('binatang/', views.binatang, name='binatang'),
    path('new_binatang/', views.new_binatang, name='new_binatang'),
    path('binatang/<int:binatang_id>/', views.detail_binatang, name='detail_binatang'),
    path('thanks', views.thanks, name='thanks'),
]