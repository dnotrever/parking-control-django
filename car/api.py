from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Car
from .serializers import CarSerializer

@api_view(['GET'])
def cars_list(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return JsonResponse(serializer.data, safe=False)

