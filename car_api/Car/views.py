from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveUpdateAPIView)
from rest_framework.response import Response

from car_api.users.permisions import IsSale, IsSupport

from .serializers import InPutCarSerializer, OutPutCarSerializer


class CarListAPiView(ListAPIView):
    permission_classes = [IsSupport,]
    serializer_class = OutPutCarSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("color","owner","number_of_cylinders")


class CarCreateAPIView(CreateAPIView):
    permission_classes = [IsSale,]
    serializer_class = InPutCarSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = InPutCarSerializer(data=request.data, context={"request": request})
            serializer.is_valid()
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_403_FORBIDDEN)

        return super().post(request, *args, **kwargs)


class UpdateRetriveCarApiView(RetrieveUpdateAPIView):
    permission_classes = []
    serializer_class = InPutCarSerializer
