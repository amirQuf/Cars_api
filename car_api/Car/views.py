from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveUpdateAPIView)
from rest_framework.response import Response
from rest_framework.views import APIView

from car_api.users.permissions import IsSale, IsSupport

from .documents import CarDocument
from .permissions import IsAuthorOrReadOnly
from .serializers import InPutCarSerializer, OutPutCarSerializer


class CarListAPiView(ListAPIView):
    permission_classes = [IsSupport,]
    serializer_class = OutPutCarSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("color", "owner", "number_of_cylinders")


class CarCreateAPIView(CreateAPIView):
    permission_classes = [IsSale,]
    serializer_class = InPutCarSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = InPutCarSerializer(
                data=request.data, context={"request": request})
            serializer.is_valid()
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_403_FORBIDDEN)

        return super().post(request, *args, **kwargs)


class UpdateRetriveCarApiView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthorOrReadOnly,]
    serializer_class = InPutCarSerializer


class CarElasticSearchAPIView(APIView):
    serializer_class = OutPutCarSerializer
    permission_classes = [IsSupport,]
    document_class = CarDocument

    def get(self, request):
        color = request.query_params.get("color")
        owner = request.query_params.get("owner")
        number_of_cylinder = request.query_params.get("cylinder")
        queryset = CarDocument.search().filter(
            owner_name=owner,
            number_of_cylinder=number_of_cylinder,
            color=color)
        if queryset:
            ''' searching Car for support using elastic search '''
            serializer = OutPutCarSerializer(data=queryset,
                                             many=True)
            serializer.is_valid()
            return Response(
                {
                    "type": "success",
                    "result": serializer.data

                }

            )
        else:
            return Response({
                "type": "error",
                "message": "user not Found."},
                status=status.HTTP_404_NOT_FOUND
            )
