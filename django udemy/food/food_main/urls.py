from . import views
from django.urls import path

app_name = 'food_main'
urlpatterns = [
     path('', views.index, name='index'),
     path('<int:item_id>/', views.details, name='details'),
     path('items1/', views.items1, name='items1'),
     path('items2/', views.items2, name='items2')
]
