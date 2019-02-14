from django.urls import path

from . import views

urlpatterns = [
    path('binatang/', views.binatang, name='binatang'),
    path('new_binatang/', views.new_binatang, name='new_binatang'),
    path('binatang/<int:post_id>/', views.post_detail, name='post_detail'),
    path('thanks', views.thanks, name='thanks'),
]