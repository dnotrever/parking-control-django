from django.db import models
from django.utils import timezone
import uuid

from account.models import User


class Car(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)

    is_parked = models.BooleanField(default=False)

    owner = models.CharField(max_length=20, blank=False, null=False)
    maker = models.CharField(max_length=10, blank=False, null=False)
    model = models.CharField(max_length=10, blank=False, null=False)
    plate = models.CharField(max_length=6, blank=False, null=False, unique=True)

    space = models.CharField(max_length=30, blank=False, null=False)
    entry = models.DateTimeField(auto_now_add=True)
    exit = models.DateTimeField(blank=True, null=True)
    value = models.DecimalField(max_digits=12, decimal_places=5)
    operator = models.ForeignKey(User, related_name='cars', on_delete=models.CASCADE)

