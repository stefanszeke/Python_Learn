from . import views
from django.urls import path

urlpatterns = [
     path('', views.index, name='index'),
     path('items1/', views.items1, name='items1'),
     path('items2/', views.items2, name='items2')
]
