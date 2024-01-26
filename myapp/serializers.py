from rest_framework import serializers
from .models import Url

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ['link', 'uuid']
