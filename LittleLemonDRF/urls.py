from django.urls import path 
from .views import RatingsView
  
urlpatterns = [
    path('ratings', RatingsView.as_view({'get': 'list', 'post': 'create'})),
]