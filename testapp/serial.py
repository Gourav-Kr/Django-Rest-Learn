from rest_framework import serializers
from .models import *

class empseri(serializers.ModelSerializer):

    class Meta:
        model=emp
        fields="__all__"