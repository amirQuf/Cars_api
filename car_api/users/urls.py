from django.urls import path, include

from .views import UserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register("user", UserViewSet)

urlpatterns = [


]
urlpatterns += router.urls
