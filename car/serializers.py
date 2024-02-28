from rest_framework import serializers

from account.serializers import UserSerializer
from .models import Car


class CarSerializer(serializers.ModelSerializer):

    operator = UserSerializer(read_only=True)

    class Meta:
        model = Car
        fields = ('id', 'owner', 'maker', 'model', 'plate', 'space', 'entry', 'exit', 'value', 'operator',)

