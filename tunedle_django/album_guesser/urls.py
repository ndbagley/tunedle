from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='tunedle-home'),
    path('about/', views.about, name='tunedle-about'),
]