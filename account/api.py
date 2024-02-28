from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

@api_view(['GET'])
def home(request):
    data = {
        'id': request.user.id,
        'name': request.user.name,
        'email': request.user.email,
    }
    return JsonResponse(data)


def test(request):
    return JsonResponse({'message': 'Testing...'})

