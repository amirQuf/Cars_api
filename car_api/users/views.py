from django.shortcuts import render
from .models import User
from rest_framework.viewsets import ModelViewSet
from .serializers import OutPutUserSerializer, InPutUserSerializer


class UserViewSet(ModelViewSet):
    queryset = Tournoment.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return OutPutUserSerializer
        else:
            return InPutUserSerializer
