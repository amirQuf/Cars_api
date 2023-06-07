from django.urls import path 
from .views import CarListAPiView , CreateAPIView

urlpatterns = [
    path('car/',CarListAPiView.as_view()),
    path('car/',CreateAPIView.as_view()),

]

