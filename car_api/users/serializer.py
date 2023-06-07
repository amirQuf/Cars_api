from rest_framework.serializers import ModelSerializer , Serializer, CharField
from .models import User

class OutPutUserSerializer(ModelSerializer) :
    role = CharField(source="get_status_display")
    class Meta:
        model =User
        fields = "__all__"


class InPutCarSerializer(ModelSerializer) :
    class Meta:
        model =User
        fields = "__all__"
