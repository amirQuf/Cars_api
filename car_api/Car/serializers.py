from rest_framework.serializers import ModelSerializer , Serializer
from .models import Car
from car_api.users.serializers import OutPutUserSerializer
from rest_framework.exceptions import ValidationError
from .documents import CarDocument


class OutPutCarSerializer(Serializer) :
    user = OutPutUserSerializer()
    class Meta:
        model = Car
        fields = ["name",
            "number_of_cylinders",
            "number_of_passengers",
            "Cylinder_volume"
            "color",
            "owner_name",
            "created",
            "modified",
            "user",]


class InPutCarSerializer(ModelSerializer) :
    

    def create(self, validated_data):
        user = self.context.get("request").user
        if user.is_anonymous:
            raise ValidationError("Anonymous user can not create post")
        validated_data["user"] = user
        return super().create(validated_data)
    
    class Meta:
        model = Car
        fields = ["name",
            "number_of_cylinders",
            "number_of_passengers",
            "Cylinder_volume",
            "color",
            "owner_name",
            "created",
            "modified",
            "user",]