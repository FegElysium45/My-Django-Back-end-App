from django.urls import path 
from . import views 

urlpatterns = [ 
       path('', views.index), 
    path('menu/', views.home, name='menu'), 
    path('register/', views.register, name='register'),  
    path('login/', views.login, name='login')
] 