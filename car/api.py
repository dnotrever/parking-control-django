from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Car
from .serializers import CarSerializer
from .forms import CarForm

@api_view(['GET'])
def cars_list(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def car_insert(request):

    form = CarForm(request.data)

    if form.is_valid():

        print('\n', request.data, '\n')

        car = form.save(commit=False)

        car.value = 10.0
        car.is_parked = True
        car.operator = request.user

        car.save()

        return JsonResponse({'status': 'success'})
    
    else:

        print('\n', 'Error!!!' '\n')

        return JsonResponse({'status': 'error'})
    

