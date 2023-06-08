from django.urls import path
from .views import CarListAPiView, CreateAPIView, UpdateRetriveCarApiView, CarElasticSearchAPIView

urlpatterns = [
    path('car/', CarListAPiView.as_view()),
    path('create/car/', CreateAPIView.as_view()),
    path('update/car/', UpdateRetriveCarApiView.as_view()),
    path('ELK/car/', CarElasticSearchAPIView.as_view()),
]
